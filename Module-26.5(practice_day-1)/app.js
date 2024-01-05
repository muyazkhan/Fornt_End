const allproduct = () => {
  fetch('https://fakestoreapi.com/products/')
    .then(res => res.json())
    .then((data) => displayallproduct(data))
    .catch((err) => console.log(err));
};

const displayallproduct = (products) => {
  products.forEach((product) => {
    console.log(product);
    const parent = document.getElementById("product-container");
    const li = document.createElement("li");
    li.innerHTML = `
      <div class="card shadow h-60 p-1">
                <div class="ratio ratio-16x9">
                  <img
                    src=${product.image}
                    class="card-img-top"
                    loading="lazy"
                    alt="..."
                  />
                </div>
                <div class="card-body p-3 p-xl-5">
                <h5 class="card-title h5 text-danger">ID: ${product.id}</h5>
                <h5 class="card-title h5 text-primary">${product.title.slice(0, 50)}</h5>
                <p class="card-title fw-bold text-warning">Category: ${product.category}</p>
                <h6 class="card-title h6 text-primary">Rating: ${product.rating.rate} Count: ${product.rating.count}</h6>
                <p class="card-text">
                  ${product.description.slice(0, 50)}
                </p>
                  <a href="#" class="btn btn-primary">Details</a>
                </div>
              </div>
      `;
    parent.appendChild(li);
  });
};

const loadCategory = () => {
  fetch("https://fakestoreapi.com/products/categories")
    .then(res => res.json())
    .then(categories => {
      const categoriesContainer = document.getElementById('categories-container');
      const list = document.createElement('ul');
      categories.forEach(category => {
        const listItem = document.createElement('li');
        listItem.textContent = category;
        list.appendChild(listItem);
        console.log(list);
      });
      categoriesContainer.appendChild(list);
    });
};

const searchByCategory = (category) => {
  fetch(`https://fakestoreapi.com/products/category/${category}`)
    .then(res => res.json())
    .then(products => {
      console.log(products);
    });
};

document.addEventListener('DOMContentLoaded', () => {
  loadCategory();
});


allproduct();