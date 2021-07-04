include "constants/datatypes.thrift"
include "constants/exceptions.thrift"

include "ad_event.thrift"
include "ad_data.thrift"
include "biz_data.thrift"
include "user_data.thrift"

namespace py adaptive.interface.adaptive
namespace cpp interface.adaptive

struct UserAdRequest
{
	1: datatypes.UserID uid,
	2: user_data.SystemInformation sysinfo,
}

struct UserAdResponse
{
	1: datatypes.Timestamp timestamp,
    2: datatypes.AdReqID adReqId,
	3: map<datatypes.AdPosition, datatypes.AdID> adids,
}

struct BizAdRequest
{
	1: datatypes.BizID bizid,
	2: ad_data.AdCreation ad_info,
	3: double daily_budget,
	4: datatypes.adaptive_int lifetime_days,
}

struct BizAdResponse
{
	1: datatypes.Timestamp timestamp,
	2: datatypes.AdID adid,
}

service Adaptive
{
	datatypes.UserID createUserAccount(1: user_data.UserAccountCreation userData)
	UserAdResponse user_request(1: UserAdRequest reqData) throws (1: exceptions.ServerException error)

	datatypes.BizID createBizAccount(1: biz_data.BizAccountCreation bizData)
	BizAdResponse biz_request(1: BizAdRequest reqData) throws (1: exceptions.ServerException error)

	oneway void registerAdEvent(1: ad_event.AdEvent adEvent)
}