from odoo.http import request
import pandas as pd
input_file_path = '../data/variant.csv'
class HandleCSV:
    def __init__(self):
        pass

    def get_store_detail_not_null_in_shopify(self):
        output_file_path = '../data/filtered_variant_charge.csv'

        df = pd.read_csv(input_file_path)

        # Filter out rows where the "Details" column is not null
        filtered_df = df[(df['Details'].notnull())
                         & (df['Event'] != 'Uninstalled')
                         & (df['Event'] != 'Install')
                         & (df['Event'] != 'Subscription charge expired')]

        # Save the filtered data to a new CSV file
        filtered_df.to_csv(output_file_path, index=False)

        print(f"Filtered data saved to {output_file_path}")

    def get_active_paid_plan_store_shopify(self):
        output_file_path = '../data/filtered_active_charge_variant.csv'
        df = pd.read_csv(input_file_path)

        # Filter rows where "Details" is not null, not "Uninstall", and not "Install"
        df_filtered = df[(df['Details'].notnull())
                         & (df['Event'] != 'Uninstalled')
                         & (df['Event'] != 'Install')
                         & (df['Event'] != 'Subscription charge expired')]


        # Sort by domain and date to identify the last event for each domain
        df_sorted = df_filtered.sort_values(by=['Shop domain', 'Date'], ascending=[True, True])

        # Get the last event for each domain
        last_events = df_sorted.groupby('Shop domain').tail(1)

        # Filter out domains where the last event is "cancel"
        df_excluded = df_filtered[
            ~df_filtered['Shop domain'].isin(last_events[last_events['Details'] == 'Subscription charge canceled']['Shop domain'])]

        # Save the filtered data to a new CSV file
        df_excluded.to_csv(output_file_path, index=False)

        print(f"Filtered data saved to {output_file_path}")

HandleCSV().get_active_paid_plan_store_shopify()