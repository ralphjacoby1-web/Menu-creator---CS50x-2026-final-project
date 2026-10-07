// Counter to give every category a unique key (c0, c1, c2...)
let counter = 0;

var amount = 0;

function addCategory() {
    const key = "c" + counter++;

    amount++;

    // Clone the category template
    const clone = document.getElementById("category-template").content.cloneNode(true);
    const category = clone.querySelector(".category");

    category.querySelector('[name="category_key"]').value = key;
    category.querySelector(".add-product").onclick = () => addProduct(category, key);
    category.querySelector(".remove-category").onclick = () => {
        category.remove();
        amount--;
        if (amount === 0) {
        addCategory();
    }
    }

    document.getElementById("categories").appendChild(category);

    // Every new category starts with one product
    addProduct(category, key);
}

function addProduct(category, key) {
    // Clone the product template
    const clone = document.getElementById("product-template").content.cloneNode(true);
    const product = clone.querySelector(".product");

    // Link the product to its category
    product.querySelector('[name="product-category"]').value = key;
    product.querySelector(".delete-product").onclick = () => product.remove();

    category.querySelector(".products").appendChild(product);
}

// This part was made with help of  claude

document.getElementById("add-category").onclick = addCategory;

addCategory();