import pandas as pd


class DashboardService:
    @staticmethod
    def overview(df: pd.DataFrame, country: str, city: str) -> dict:
        df_copy = df.copy(deep=True)
        df_copy = df_copy[(df_copy.country == country) & (df_copy.city == city)]

        average_price = df_copy.price.mean().round(2).item()
        property_type_counts = df_copy["property_type"].value_counts()
        total_properties = property_type_counts.sum().item()

        return {
            "total_properties": total_properties,
            "average_price": average_price,
            "property_type_counts": property_type_counts.to_dict(),
        }
