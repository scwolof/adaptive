/**
 * Autogenerated by Thrift Compiler (0.11.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef ad_event_TYPES_H
#define ad_event_TYPES_H

#include <iosfwd>

#include <thrift/Thrift.h>
#include <thrift/TApplicationException.h>
#include <thrift/TBase.h>
#include <thrift/protocol/TProtocol.h>
#include <thrift/transport/TTransport.h>

#include <thrift/stdcxx.h>
#include "datatypes_types.h"


namespace interface { namespace ad_event {

struct AdEventType {
  enum type {
    UNKNOWN = 0,
    IMPRESSION = 1,
    CLICK = 2
  };
};

extern const std::map<int, const char*> _AdEventType_VALUES_TO_NAMES;

std::ostream& operator<<(std::ostream& out, const AdEventType::type& val);

class AdEvent;

typedef struct _AdEvent__isset {
  _AdEvent__isset() : timestamp(false), uid(false), adid(false), adReqId(false), eventType(true) {}
  bool timestamp :1;
  bool uid :1;
  bool adid :1;
  bool adReqId :1;
  bool eventType :1;
} _AdEvent__isset;

class AdEvent : public virtual ::apache::thrift::TBase {
 public:

  AdEvent(const AdEvent&);
  AdEvent& operator=(const AdEvent&);
  AdEvent() : timestamp(0), uid(0), adid(0), adReqId(0), eventType((AdEventType::type)0) {
    eventType = (AdEventType::type)0;

  }

  virtual ~AdEvent() throw();
   ::interface::constants::datatypes::Timestamp timestamp;
   ::interface::constants::datatypes::UserID uid;
   ::interface::constants::datatypes::AdID adid;
   ::interface::constants::datatypes::AdReqID adReqId;
  AdEventType::type eventType;

  _AdEvent__isset __isset;

  void __set_timestamp(const  ::interface::constants::datatypes::Timestamp val);

  void __set_uid(const  ::interface::constants::datatypes::UserID val);

  void __set_adid(const  ::interface::constants::datatypes::AdID val);

  void __set_adReqId(const  ::interface::constants::datatypes::AdReqID val);

  void __set_eventType(const AdEventType::type val);

  bool operator == (const AdEvent & rhs) const
  {
    if (!(timestamp == rhs.timestamp))
      return false;
    if (!(uid == rhs.uid))
      return false;
    if (!(adid == rhs.adid))
      return false;
    if (!(adReqId == rhs.adReqId))
      return false;
    if (!(eventType == rhs.eventType))
      return false;
    return true;
  }
  bool operator != (const AdEvent &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const AdEvent & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

  virtual void printTo(std::ostream& out) const;
};

void swap(AdEvent &a, AdEvent &b);

std::ostream& operator<<(std::ostream& out, const AdEvent& obj);

}} // namespace

#endif
