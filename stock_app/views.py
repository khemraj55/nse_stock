from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse
from django.views import View
from .nse import NseIndia

class LiveStockDataView(View):
    def get(self, request, symbol):
        nse = NseIndia()

        try:
            TCap, FCap, LPrice, Macro, Sector, Industry, BIndustry = nse.get_stock_info(symbol)
            stock_data = {
                "symbol": symbol,
                "total_cap": TCap,
                "free_float_cap": FCap,
                "last_price": LPrice,
                "macro": Macro,
                "sector": Sector,
                "industry": Industry,
                "basic_industry": BIndustry,
            }

            # Create a DataFrame from the stock data
            df = pd.DataFrame([stock_data])

            # Save to Excel file
            df.to_excel('stock_data.xlsx', index=False)

            return JsonResponse(stock_data)
        except Exception as e:
            return JsonResponse({"error": f"Error fetching and saving stock data for symbol {symbol}: {e}"}, status=500)

class ExtractStockDataView(View):
    def get(self, request):
        try:
            # Read data from Excel file into a DataFrame
            df = pd.read_excel('stock_data.xlsx')

            # Convert DataFrame to JSON
            data_json = df.to_json(orient='records')

            return JsonResponse({"data": data_json})
        except Exception as e:
            return JsonResponse({"error": f"Error extracting stock data: {e}"}, status=500)
