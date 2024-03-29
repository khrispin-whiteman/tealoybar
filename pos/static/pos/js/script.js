var product_ids = [];
var total_price = 0;

function addItem(item_id, item_name, item_price) {
  var tableBody = document.getElementById('summary-table-body');
  var tr = document.createElement('tr');

  var td_name = document.createElement('td');
  td_name.innerHTML = item_name;

  var td_price = document.createElement('td');
  td_price.setAttribute('class', 'text-right');
  td_price.innerHTML = 'K' + item_price;

  total_price += item_price;

  tr.appendChild(td_name);
  tr.appendChild(td_price);

  clearTotal();

  tableBody.appendChild(tr);
  tableBody.appendChild(getTotal());

  product_ids.push(item_id);
}

// function addItemByBarcode() {
//                 //alert('Inside addItemByBarcode');
//                 var barcode = document.getElementById("barcode_id").value;
//
//                 alert('Var Acquired: ' + barcode);
//                 $.ajax(
//                     {
//                         type: 'GET',
//                         url: 'ajaxgetproduct',
//                         data: {product_barcode: barcode},
//                         dataType: 'json',
//                         success: function (product_response) {
//
//                             //get the returned data into varriables
//                             item_id = product_response.pk;
//                             item_name = product_response.productname;
//                             item_price = product_response.price;
//
//                             var tableBody = document.getElementById('summary-table-body');
//                             var tr = document.createElement('tr');
//
//                             var td_name = document.createElement('td');
//                             td_name.innerHTML = item_name;
//
//                             var td_price = document.createElement('td');
//                             td_price.setAttribute('class', 'text-right');
//                             td_price.innerHTML = 'K' + item_price;
//
//                             total_price += item_price;
//
//                             tr.appendChild(td_name);
//                             tr.appendChild(td_price);
//
//                             clearTotal();
//
//                             tableBody.appendChild(tr);
//                             tableBody.appendChild(getTotalOfPrices());
//
//                             product_ids.push(item_id);
//
//
//                             alert("PRODUCT_NAME: " + product_response.productname + " PRICE: " + product_response.price);
//                         },
//
//                     }
//                 );
//
//             }
//

function clearAllItems() {
  alert('Testing');
  var table = document.getElementById('summary-table-body');
  while (table.firstChild) {
    table.removeChild(table.firstChild);
  }

  product_ids = [];
  total_price = 0;

  table.appendChild(getTotal());
}

function clearTotal() {
  var total_tr = document.getElementById("total-tr");
  if (total_tr !== null) {
    total_tr.parentNode.removeChild(total_tr);
  }
}

function getTotal(){
  var tr_total = document.createElement('tr');
  tr_total.setAttribute('id', 'total-tr')

  var td_total_display = document.createElement('td');
  td_total_display.setAttribute('class', 'thick-line text-right');
  td_total_display.innerHTML = "<strong>Total: </strong>";

  var td_total_price = document.createElement('td');
  td_total_price.setAttribute('class', 'thick-line text-right');
  td_total_price.innerHTML = "<strong>K" + total_price + " </strong>";

  tr_total.appendChild(td_total_display);
  tr_total.appendChild(td_total_price);

  return tr_total;
}

function postOrder(url, cust_id) {
  data = {
    'customer_id' : cust_id,
    'product_ids' : product_ids,
    'total_price' : total_price,
  };

  let csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0];

  let form = document.createElement('form');
  form.action = url;
  form.method = "POST";

  let inp = document.createElement('input');
  inp.type = 'hidden';
  inp.name = 'data';
  inp.value = JSON.stringify(data);

  form.appendChild(csrftoken);
  form.appendChild(inp);

  document.body.appendChild(form);
  form.submit();
}
