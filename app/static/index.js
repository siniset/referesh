const FieldContainer = document.createElement("div")
FieldContainer.classList.add("reference-field-container", "vertical", "flex", "v-gap-lg")

const changeButton = document.createElement("b")
changeButton.classList.add("button", "button-dark", "text-bold")
changeButton.textContent = "Muuta"
FieldContainer.appendChild(changeButton)

const deleteButton = document.createElement("a")
deleteButton.classList.add("button", "button-dark", "text-bold")
deleteButton.textContent = "Poista"
FieldContainer.appendChild(deleteButton)

const FieldView = document.createElement("div")
FieldView.classList.add("field")

async function toggleReferenceView(id) {
  const referenceView = document.querySelector(`[data-reference-id='${id}']`)

  if (referenceView.classList.toggle("open")) {
    const referenceData = await fetchReferenceData(id)
    const fieldContainer = FieldContainer.cloneNode(true)

    fieldContainer.prepend(
      ...Object.entries(referenceData).map(([name, content]) => {
        const view = FieldView.cloneNode(false)
        view.textContent = `${name}: ${content}`
        return view
      })
    )

    referenceView.appendChild(fieldContainer)
    fieldContainer.lastChild.href = `/delete/${id}`
  } else {
    referenceView.querySelector(".reference-field-container").remove()
  }
}


async function fetchReferenceData(id) {
  const reference = await fetch(`/references/${id}`)
  return reference.json()
}
