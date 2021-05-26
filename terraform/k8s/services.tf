resource "kubernetes_service" "app-master" {
  metadata {
    name = "app-master"
  }

  spec {
    selector = {
      app  = "djangodemo"
    }
    port {
      name        = "app-port"
      port        = 8080
      target_port = 8080
    }


    type = "LoadBalancer"
  }
  
}
