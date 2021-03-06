/**
 * Autogenerated by Thrift Compiler (0.11.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef biz_data_TYPES_H
#define biz_data_TYPES_H

#include <iosfwd>

#include <thrift/Thrift.h>
#include <thrift/TApplicationException.h>
#include <thrift/TBase.h>
#include <thrift/protocol/TProtocol.h>
#include <thrift/transport/TTransport.h>

#include <thrift/stdcxx.h>


namespace interface { namespace biz_data {

class BizAccountCreation;

typedef struct _BizAccountCreation__isset {
  _BizAccountCreation__isset() : name(false) {}
  bool name :1;
} _BizAccountCreation__isset;

class BizAccountCreation : public virtual ::apache::thrift::TBase {
 public:

  BizAccountCreation(const BizAccountCreation&);
  BizAccountCreation& operator=(const BizAccountCreation&);
  BizAccountCreation() : name() {
  }

  virtual ~BizAccountCreation() throw();
  std::string name;

  _BizAccountCreation__isset __isset;

  void __set_name(const std::string& val);

  bool operator == (const BizAccountCreation & rhs) const
  {
    if (!(name == rhs.name))
      return false;
    return true;
  }
  bool operator != (const BizAccountCreation &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const BizAccountCreation & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

  virtual void printTo(std::ostream& out) const;
};

void swap(BizAccountCreation &a, BizAccountCreation &b);

std::ostream& operator<<(std::ostream& out, const BizAccountCreation& obj);

}} // namespace

#endif
