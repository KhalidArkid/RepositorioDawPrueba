// Coordenada inicial
class Coordenada {
    var x: Int = 0
    var y: Int = 0
}


// Funciones de movimiento
fun Coordenada.moure_dreta() {
    x += 1
}

fun Coordenada.moure_esquerra() {
    x -= 1
}

fun Coordenada.moure_amunt() {
    y += 1
}

fun Coordenada.moure_avall() {
    y -= 1
}


// Programa principal
fun main() {
    val coordenada = Coordenada()
    coordenada.moure_dreta()
    println("Nova coordenada després de moure a la dreta: (${coordenada.x}, ${coordenada.y})")

    coordenada.moure_amunt()
    println("Nova coordenada després de moure amunt: (${coordenada.x}, ${coordenada.y})")
}


