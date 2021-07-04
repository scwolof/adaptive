include "constants/datatypes.thrift"
include "constants/user_attributes.thrift"

namespace py adaptive.interface.user_data
namespace cpp interface.user_data

struct UserAccountCreation
{
	1: string name
	2: datatypes.adaptive_int age
	3: user_attributes.Gender gender
}

struct SystemInformation
{
	1: user_attributes.DeviceType device = user_attributes.DeviceType.UNKNOWN,
}
