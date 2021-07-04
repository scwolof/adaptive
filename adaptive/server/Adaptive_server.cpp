#include<iostream>

#include "interface/Adaptive.h"
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/server/TSimpleServer.h>
#include <thrift/transport/TServerSocket.h>
#include <thrift/transport/TBufferTransports.h>

using namespace ::apache::thrift;
using namespace ::apache::thrift::protocol;
using namespace ::apache::thrift::transport;
using namespace ::apache::thrift::server;

using namespace  ::interface::adaptive;

class AdaptiveHandler : virtual public AdaptiveIf {
 public:
  AdaptiveHandler() {
    // Your initialization goes here
  }

   ::interface::constants::datatypes::UserID createUserAccount(const  ::interface::user_data::UserAccountCreation& userData) {
    // Your implementation goes here
    std::cout << "Create account: " << userData.name << std::endl;
    return 0;
  }

  void user_request(UserAdResponse& _return, const UserAdRequest& reqData) {
    // Your implementation goes here
    printf("user_request\n");
  }

   ::interface::constants::datatypes::BizID createBizAccount(const  ::interface::biz_data::BizAccountCreation& bizData) {
    // Your implementation goes here
    printf("createBizAccount\n");
  }

  void biz_request(BizAdResponse& _return, const BizAdRequest& reqData) {
    // Your implementation goes here
    printf("biz_request\n");
  }

  void registerAdEvent(const  ::interface::ad_event::AdEvent& adEvent) {
    // Your implementation goes here
    printf("registerAdEvent\n");
  }

};

int main(int argc, char **argv) {
  int port = 9090;
  ::apache::thrift::stdcxx::shared_ptr<AdaptiveHandler> handler(new AdaptiveHandler());
  ::apache::thrift::stdcxx::shared_ptr<TProcessor> processor(new AdaptiveProcessor(handler));
  ::apache::thrift::stdcxx::shared_ptr<TServerTransport> serverTransport(new TServerSocket(port));
  ::apache::thrift::stdcxx::shared_ptr<TTransportFactory> transportFactory(new TBufferedTransportFactory());
  ::apache::thrift::stdcxx::shared_ptr<TProtocolFactory> protocolFactory(new TBinaryProtocolFactory());

  TSimpleServer server(processor, serverTransport, transportFactory, protocolFactory);
  server.serve();
  return 0;
}

