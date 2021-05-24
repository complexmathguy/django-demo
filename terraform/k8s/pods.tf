resource "kubernetes_replication_controller" "app-master" {
  metadata {
    name = "app-master"
  }

  spec {
    replicas = 1

    selector = {
      app  = "djangodemo"
    }
    template {        
      container {
        image = "theharbormaster/django-demo:latest"
        name  = "app-container"
        
        port {
          container_port = 8080
        }
      }
    }
  }
}