include "constants/user_attributes.thrift"

namespace py adaptive.interface.ad_data
namespace cpp interface.ad_data

struct AdTargeting
{
    1: user_attributes.Gender gender,
    2: user_attributes.DeviceType device_type,
}

enum AdObjectiveType
{
    UNKNOWN = 0,
    IMPRESSION = 1,
    CLICK = 2,
}

enum AdCategory
{
    UNKNOWN = 0,
    BRAND = 1,
    GAMES = 2,
    TRAVEL = 3,
    ECOMMERCE = 4,
    MEDIA = 5,
}

struct AdCreation
{
	1: AdTargeting targeting,
    2: AdObjectiveType objective,
    3: AdCategory category,
    4: double max_bid = -1,
}
