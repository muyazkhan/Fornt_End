const loadData = () => {
  const searchText = document.getElementById("search-text").value;
  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=${searchText}`)
    .then((response) => response.json())
    .then((data) => displayData(data.meals));
};

// const displayData = (data) => {
//   console.log(data);
// };

const displayData = (data) => {
  document.getElementById("total-food").innerText=data.length;
  
};
