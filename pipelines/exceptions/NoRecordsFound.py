class NoRecordsFound(Exception):
    def __init__(self, data_point_name):
        message = f"No Records found for : {data_point_name}"
        super().__init__(message)
        self.data_point_name = data_point_name


print(f"NoRecordsFound type: {type(NoRecordsFound)}")