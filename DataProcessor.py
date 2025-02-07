import pandas as pd
import re

class DataProcessor:
    @staticmethod
    def fill_missing_values(df, columns_to_check_build=['offer_url', 'add_info', 'rest_info'], 
                           columns_to_check_floors=['offer_url-href', 'offer_url']):
        """
        Comprehensive function to fill missing values for both build_type and total_floors
        based on regex patterns found in specified columns.
        
        Args:
            df: DataFrame to process
            columns_to_check_build: List of columns to search for building patterns
            columns_to_check_floors: List of columns to search for floor patterns
        Returns:
            DataFrame with filled build_type and total_floor values
        """
        
        # Define building type patterns
        build_patterns = [
            (r'apartament|apartamentow', 'apartamentowiec'),
            (r'\bblok|bloku\b', 'blok'),
            (r'kamienic[ay]', 'kamienica'),
            (r'\bdom\b|\bdwor|rezydencj', 'dom'),
            (r'szereg|blizniak', 'szeregowiec')
        ]
        
        # Define floor patterns
        floor_patterns = [
            (r'Liczba\s+pi[ęe]ter:?\s*(\d+)', 1),
            (r'(\d+)[-\s]?pi[ęe]trow[eya]', 1),
            (r'(\d+)[-\s]?poziomow[eya]', 1),
            (r'pi[ęe]tro:?\s*\d+/(\d+)', 1)
        ]
        
        # Create a copy of the dataframe to avoid modifying the original
        df = df.copy()
        
        # Process build_type
        mask_build = df['build_type'].isna()
        for idx in df[mask_build].index:
            row_text = ' '.join(str(df.loc[idx, col]).lower() 
                              for col in columns_to_check_build 
                              if pd.notna(df.loc[idx, col]))
            
            for pattern, value in build_patterns:
                if re.search(pattern, row_text):
                    df.loc[idx, 'build_type'] = value
                    break
        
        # Process total_floor
        mask_floor = df['total_floor'].isna()
        for idx in df[mask_floor].index:
            row_text = ' '.join(str(df.loc[idx, col]).lower() 
                              for col in columns_to_check_floors 
                              if pd.notna(df.loc[idx, col]))
            
            for pattern, group in floor_patterns:
                match = re.search(pattern, row_text)
                if match:
                    try:
                        df.loc[idx, 'total_floor'] = int(match.group(group))
                        break
                    except (ValueError, IndexError):
                        continue
        
        return df