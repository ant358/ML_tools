import pgeocode
import pandas as pd
# select uk (gb)region
nomi = pgeocode.Nominatim('gb')


def postcode_to_lat_long(df, postcode):
    """Function to convert GB postcode's to latitude
     and longitutde.

    Args:
        df (pandas dataframe): dataframe with postcode column
        postcode (str): postcode column to be converted

    Returns:
        df (pandas dataframe): dataframe with
                               latitude and longitude columns
    """
    # Take just the postcode column
    df = df[[postcode]].sort_values(by=[postcode])
    # drop any duplicated postcodes
    df.drop_duplicates(keep='first', inplace=True)
    # reset the index
    df.reset_index(inplace=True, drop=True)
    try:
        # Look up lat long for all the postcodes
        df["latitude"] = df[postcode].apply(
            lambda x: nomi.query_postal_code(x)[9])
        df["longitude"] = df[postcode].apply(
            lambda x: nomi.query_postal_code(x)[10])
    except TypeError:
        df["latitude"] = None
        df["longitude"] = None

    return df


if __name__ == "__main__":
    # load the data with your postcodes
    df = pd.read_csv('./postcodes.csv')
    df_postcode_lat_long = postcode_to_lat_long(df, 'Postcode')
    # export to csv
    df_postcode_lat_long.to_csv("./postcode_lat_long_.csv",
                                index=False)
