Ex1: 

variable "input_variable" {
  description = "Input variable to be written to film.txt"
}

resource "null_resource" exo1 {
    provisioner "local-exec" {
        command = "echo '${var.input_variable}' >> film.txt"
    }
}



Ex2:
variable "input_variable" {
  default = {
    "film1":"LOL"
  }
}

resource "null_resource" exo3 {
    for_each = var.input_variable
    triggers = {
        foo = each.value
    }
    provisioner "local-exec" {
        command = "echo '${each.key} ${each.value}' >> film.txt"
    }
}

