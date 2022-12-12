const FieldContainer = document.createElement("div")
FieldContainer.classList.add("reference-field-container", "vertical", "flex", "v-gap-lg")

const changeButton = document.createElement("a")
changeButton.id = "change-button"
changeButton.classList.add("button", "button-dark", "text-bold")
changeButton.textContent = "Muuta"
FieldContainer.appendChild(changeButton)

const deleteButton = document.createElement("a")
deleteButton.classList.add("button", "button-dark", "text-bold")
deleteButton.textContent = "Poista"
FieldContainer.appendChild(deleteButton)

const FieldView = document.createElement("div")
FieldView.classList.add("field")

Array.from(document.querySelectorAll(".reference")).forEach(ref => {
  ref.children[0].onclick = () => {
    toggleReferenceView(ref.dataset.referenceId)
  }
})

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
    document.getElementById("change-button").href = `/references/edit/${id}`
    fieldContainer.lastChild.href = `/delete/${id}`
  } else {
    referenceView.querySelector(".reference-field-container").remove()
  }
}


async function fetchReferenceData(id) {
  const reference = await fetch(`/references/${id}`)
  return reference.json()
}
