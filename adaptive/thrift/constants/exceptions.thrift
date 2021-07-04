namespace py adaptive.interface.constants.exceptions
namespace cpp interface.constants.error_codes

enum ErrorCode
{
	UNKNOWN = 0,
}

const map<ErrorCode, string> ErrorDescription = {
	ErrorCode.UNKNOWN: "Unknown error",
}

exception ServerException
{
    1: ErrorCode error_code,
    2: string error_description
}