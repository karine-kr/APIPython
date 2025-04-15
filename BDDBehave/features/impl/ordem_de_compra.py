import requests
from datetime import datetime
  
class OrdemDeCompra:
      def __init__(self):
          self.url_petstore_order = 'https://petstore.swagger.io/v2/store/order'
          self.id = None
          self.petId = None
          self.quantidade = None
          self.data = datetime.now().isoformat()
          self.status_code = None
  
      def post_criar_uma_nova_ordem(self):
          header = {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
          }
  
          data = {
            "id": self.id,
            "petId": self.petId,
            "quantity": self.quantidade,
            "shipDate":  self.data,
            "status": "placed",
            "complete": True
          }
          response = requests.post(self.url_petstore_order, headers=header, json=data)
          self.status_code = response.status_code
          self.response = response
          return response
      
      
      def get_buscar_ordem_pelo_id(self,orderId):
             header = {
              'Accept': 'application/json',
          }
             data = {
            "ordemId": self.id
          }
             
             self.response = requests.get(f"{self.url_petstore_order}/{orderId}")
             self.status_code = self.response.status_code
             return self.response
           