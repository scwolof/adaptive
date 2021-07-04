include "constants/datatypes.thrift"

namespace py adaptive.interface.ad_event
namespace cpp interface.ad_event

enum AdEventType
{
	UNKNOWN = 0,
	IMPRESSION = 1,
	CLICK = 2,
}

struct AdEvent
{
	1: datatypes.Timestamp timestamp,
   	2: datatypes.UserID uid,
    3: datatypes.AdID adid,
    4: datatypes.AdReqID adReqId,
    5: AdEventType eventType = AdEventType.UNKNOWN,
}