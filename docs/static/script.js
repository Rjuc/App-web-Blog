const boton = document.getElementById("like");

if (boton) {
    const clave = `me-gusta-${boton.dataset.entrada}`;
    const actualizar = () => {
        const marcado = localStorage.getItem(clave) === "si";
        boton.setAttribute("aria-pressed", marcado);
        boton.textContent = marcado ? "Te gusta esta entrada (" : "Me gusta (";
        const numero = document.createElement("span");
        numero.id = "contador";
        numero.textContent = marcado ? "1" : "0";
        boton.append(numero, document.createTextNode(")"));
    };

    boton.addEventListener("click", () => {
        const marcado = localStorage.getItem(clave) === "si";
        localStorage.setItem(clave, marcado ? "no" : "si");
        actualizar();
    });

    actualizar();
}
