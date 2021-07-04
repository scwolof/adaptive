/**
 * Autogenerated by Thrift Compiler (0.11.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "user_data_types.h"

#include <algorithm>
#include <ostream>

#include <thrift/TToString.h>

namespace interface { namespace user_data {


UserAccountCreation::~UserAccountCreation() throw() {
}


void UserAccountCreation::__set_name(const std::string& val) {
  this->name = val;
}

void UserAccountCreation::__set_age(const  ::interface::constants::datatypes::adaptive_int val) {
  this->age = val;
}

void UserAccountCreation::__set_gender(const  ::interface::constants::user_attributes::Gender::type val) {
  this->gender = val;
}
std::ostream& operator<<(std::ostream& out, const UserAccountCreation& obj)
{
  obj.printTo(out);
  return out;
}


uint32_t UserAccountCreation::read(::apache::thrift::protocol::TProtocol* iprot) {

  ::apache::thrift::protocol::TInputRecursionTracker tracker(*iprot);
  uint32_t xfer = 0;
  std::string fname;
  ::apache::thrift::protocol::TType ftype;
  int16_t fid;

  xfer += iprot->readStructBegin(fname);

  using ::apache::thrift::protocol::TProtocolException;


  while (true)
  {
    xfer += iprot->readFieldBegin(fname, ftype, fid);
    if (ftype == ::apache::thrift::protocol::T_STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->name);
          this->__isset.name = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 2:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          xfer += iprot->readI32(this->age);
          this->__isset.age = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 3:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          int32_t ecast0;
          xfer += iprot->readI32(ecast0);
          this->gender = ( ::interface::constants::user_attributes::Gender::type)ecast0;
          this->__isset.gender = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      default:
        xfer += iprot->skip(ftype);
        break;
    }
    xfer += iprot->readFieldEnd();
  }

  xfer += iprot->readStructEnd();

  return xfer;
}

uint32_t UserAccountCreation::write(::apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  ::apache::thrift::protocol::TOutputRecursionTracker tracker(*oprot);
  xfer += oprot->writeStructBegin("UserAccountCreation");

  xfer += oprot->writeFieldBegin("name", ::apache::thrift::protocol::T_STRING, 1);
  xfer += oprot->writeString(this->name);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("age", ::apache::thrift::protocol::T_I32, 2);
  xfer += oprot->writeI32(this->age);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("gender", ::apache::thrift::protocol::T_I32, 3);
  xfer += oprot->writeI32((int32_t)this->gender);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(UserAccountCreation &a, UserAccountCreation &b) {
  using ::std::swap;
  swap(a.name, b.name);
  swap(a.age, b.age);
  swap(a.gender, b.gender);
  swap(a.__isset, b.__isset);
}

UserAccountCreation::UserAccountCreation(const UserAccountCreation& other1) {
  name = other1.name;
  age = other1.age;
  gender = other1.gender;
  __isset = other1.__isset;
}
UserAccountCreation& UserAccountCreation::operator=(const UserAccountCreation& other2) {
  name = other2.name;
  age = other2.age;
  gender = other2.gender;
  __isset = other2.__isset;
  return *this;
}
void UserAccountCreation::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "UserAccountCreation(";
  out << "name=" << to_string(name);
  out << ", " << "age=" << to_string(age);
  out << ", " << "gender=" << to_string(gender);
  out << ")";
}


SystemInformation::~SystemInformation() throw() {
}


void SystemInformation::__set_device(const  ::interface::constants::user_attributes::DeviceType::type val) {
  this->device = val;
}
std::ostream& operator<<(std::ostream& out, const SystemInformation& obj)
{
  obj.printTo(out);
  return out;
}


uint32_t SystemInformation::read(::apache::thrift::protocol::TProtocol* iprot) {

  ::apache::thrift::protocol::TInputRecursionTracker tracker(*iprot);
  uint32_t xfer = 0;
  std::string fname;
  ::apache::thrift::protocol::TType ftype;
  int16_t fid;

  xfer += iprot->readStructBegin(fname);

  using ::apache::thrift::protocol::TProtocolException;


  while (true)
  {
    xfer += iprot->readFieldBegin(fname, ftype, fid);
    if (ftype == ::apache::thrift::protocol::T_STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          int32_t ecast3;
          xfer += iprot->readI32(ecast3);
          this->device = ( ::interface::constants::user_attributes::DeviceType::type)ecast3;
          this->__isset.device = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      default:
        xfer += iprot->skip(ftype);
        break;
    }
    xfer += iprot->readFieldEnd();
  }

  xfer += iprot->readStructEnd();

  return xfer;
}

uint32_t SystemInformation::write(::apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  ::apache::thrift::protocol::TOutputRecursionTracker tracker(*oprot);
  xfer += oprot->writeStructBegin("SystemInformation");

  xfer += oprot->writeFieldBegin("device", ::apache::thrift::protocol::T_I32, 1);
  xfer += oprot->writeI32((int32_t)this->device);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(SystemInformation &a, SystemInformation &b) {
  using ::std::swap;
  swap(a.device, b.device);
  swap(a.__isset, b.__isset);
}

SystemInformation::SystemInformation(const SystemInformation& other4) {
  device = other4.device;
  __isset = other4.__isset;
}
SystemInformation& SystemInformation::operator=(const SystemInformation& other5) {
  device = other5.device;
  __isset = other5.__isset;
  return *this;
}
void SystemInformation::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "SystemInformation(";
  out << "device=" << to_string(device);
  out << ")";
}

}} // namespace
