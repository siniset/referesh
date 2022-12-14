const references = document.querySelectorAll(".reference")

references.forEach(reference =>
  reference
    .firstElementChild
  .addEventListener("click", () => handleHeaderClick(reference.dataset.referenceId)))

function fetchField(referenceId) {
  return fetch(`/references/${referenceId}`)
    .then(response => response.json())
}

function createFieldElement(field) {
  const [name, content] = field
  
  const fieldElement = document.createElement("div")
  fieldElement.classList.add("field", "flex", "h-gap-md")

  const nameElement = document.createElement("div")
  nameElement.textContent = name[0].toUpperCase() + name.slice(1) + ":"
  nameElement.classList.add("text-bold")

  const contentElement = document.createElement("div")
  contentElement.textContent = content;

  fieldElement.append(nameElement, contentElement)

  return fieldElement
}

async function openReferenceView(referenceElement) {
  const body = document.createElement("div")
  body.classList.add("reference-body")

  const fieldList = document.createElement("div")
  fieldList.classList.add("field-list", "v-gap-md")

  const deleteButton = document.createElement("a")
  deleteButton.textContent = "Poista"
  deleteButton.classList.add("button", "button-dark", "text-bold")
  deleteButton.href = `/delete/${referenceElement.dataset.referenceId}`

  referenceElement.appendChild(body) 
  body.appendChild(fieldList) 
  body.appendChild(deleteButton) 
  
  fetchField(referenceElement.dataset.referenceId)
    .then(Object.entries)
    .then(fields => fields.filter(([name]) => name !== "title"))
    .then(fields => fieldList.append(...fields.map(createFieldElement)))
}

function closeReferenceView(element) {
  element.querySelector(".reference-body").remove()
}

function toggleReferenceView(referenceElement) {
  const isOpen = referenceElement.classList.toggle("open")

  if (isOpen) {
    openReferenceView(referenceElement)
  } else {
    closeReferenceView(referenceElement)
  }
}

function handleHeaderClick(referenceId) {
  const referenceElement = document.querySelector(`.reference[data-reference-id="${referenceId}"]`)

  toggleReferenceView(referenceElement)
}
