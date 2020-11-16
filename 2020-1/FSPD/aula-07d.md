# Exemplo de Uso de gRPC

Pacote RCP focado no desenvolvimento multi linguagem

Exige compilação do arquivo de interface

Utiliza serialização por protocol buffers

Serialização é visível pro programador, vc precisa saber que está usando um procesimento RPC por precisa serializar e fazer uma chamada especial.

Servidor básico em python: Thread pool

Pode incluir registry, autenticação e criptografia.

Quatro tipos de chamamas:
1. Unary: Normal
2. Pipelines:
   1. server streaming
   2. client streaming
   3. bidirectional


Execução assíncrona com método `future`.

Execução pode ser temporizada

# Implementação

### Interface
```Protobuff
/* Arquivo de definição da interface entre cliente e servidor
 * Estamos usando a versão 3 de protocol buffers 
 */
syntax = "proto3";

// Nome do pacote 
package hello;

service DoStuff {
  /* Estamos definindo dois métdos; em ambos o parâmetro
   *   é do tipo HelloRequest e a resposta é do tipo HelloReply.
   */
  rpc say_hello (HelloRequest) returns (HelloReply) {}
  rpc say_hello_again (HelloRequest) returns (HelloReply) {}
}

// HelloRequest tem apenas um campo, que é o pid do cliente
message HelloRequest {
  int32 pid = 1;  // Cada campo deve ser numerado
}

// A resposta também só tem um componente, um string
message HelloReply {
  string retval = 1;
}
```

### Server
```Python
from concurrent import futures # usado na definição do pool de threads

import grpc

import hello_pb2, hello_pb2_grpc # módulos gerados pelo compilador de gRPC

# Os procedimentos oferecidos aos clientes precisam ser encapsulados
#   em uma classe que herda do código do stub.
class DoStuff(hello_pb2_grpc.DoStuffServicer):

   # A assinatura de todos os procedimentos é igual: um objeto com os
   # parâmetros e outro com o contexto de execução do servidor
   def say_hello(self, request, context):
      print("GRPC server in say_hello, pid =" , str(request.pid))
      return hello_pb2.HelloReply(retval='Hello, %d!' % request.pid)

   # Mesmo princípio para o segundo procedimento.
   def say_hello_again(self, request, context):
      print("GRPC server in say_hello_again, pid =" , str(request.pid))
      return hello_pb2.HelloReply(retval='Hello again, %d!' % request.pid)

def serve():
   # O servidor usa um modelo de pool de threads do pacote concurrent
   server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
   # O servidor precisa ser ligado ao objeto que identifica os
   #   procedimentos a serem executados.
   hello_pb2_grpc.add_DoStuffServicer_to_server(DoStuff(), server)
   # O método add_insecure_port permite a conexão direta por TCP
   #   Outros recursos estão disponíveis, como uso de um registry
   #   (dicionário de serviços), criptografia e autenticação.
   server.add_insecure_port('localhost:8888')
   # O servidor é iniciado e esse código não tem nada para fazer
   #   a não ser esperar pelo término da execução.
   server.start()
   server.wait_for_termination()

if __name__ == '__main__':
    serve()
```

### Cliente
```Python
from __future__ import print_function # usado internamente nos stubs
import os # para usar getpid

import grpc

import hello_pb2, hello_pb2_grpc # módulos gerados pelo compilador de gRPC

def run():
    # Primeiro, é preciso abrir um canal para o servidor
    channel = grpc.insecure_channel('localhost:8888')
    # E criar o stub, que vai ser o objeto com referências para os
    # procedimentos remotos (código gerado pelo compilador)
    stub = hello_pb2_grpc.DoStuffStub(channel)

    my_pid = os.getpid()

    # Primeira chamada: é preciso serializar o parâmetro usando
    #   o código gerado pelo compilador
    # A desserialização do valor de retorno é feita internamente pelo stub
    response = stub.say_hello(hello_pb2.HelloRequest(pid=my_pid))
    print("GRPC client received: " + response.retval)

    # Segunda chamada: mesmo princípio
    response = stub.say_hello_again(hello_pb2.HelloRequest(pid=my_pid))
    print("GRPC client received: " + response.retval)
    
    # Ao final o cliente pode fechar o canal para o servidor.
    channel.close()


if __name__ == '__main__':
    run()
```