class NoMatchingProductsFound(Exception):
    def __init__(self):
        message = f"No Matching Products Found for this search Criteria , please update the query"
        super().__init__(message)
