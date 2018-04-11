module.exports = {
      add: function(num1, num2) { 
           // add code here 
           console.log(`the sum is: ${num1 + num2}`)
      },
      multiply: function(num1, num2) {
           // add code here 
           console.log(`the product is: ${num1 * num2}`)
      },
      square: function(num) {
           // add code here 
           console.log(`squared product is: ${num * num}`)
      },
      random: function(num1, num2) {
           // add code here
           let range = (num2 - num1) + .9;
           let ran = Math.floor(Math.random() * range) + num1;
           console.log(`random number: ${ran}`)
      }
  };