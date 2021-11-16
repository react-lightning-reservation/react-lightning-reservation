# React Lightning Reservation

We are developing a React.JS button which corresponds to a booking of a single-customer event, such as a surfing lesson. 
- The user can list the available time slots for each surfing instructor.
- The user can book the selected surfing lesson, which indicates the instructor and the start and end time.
- The booking can be secured via Bitcoin payment via the Lightning Neetwork. 
- An Invoice pops up on the screeen as soon as the user clicks on the "Reserve" button.
- The user can point to the QR-code of the Lightning Network invoice or simply copy it.
- As soon as the user completes the payment, the lesson is secured and the reservation is guaranteed with the deposit. 

## Front end

The Front end is written in JavaScript and uses React.JS.

The **React Booking Button** is a simeple React functional component can be can be placed anywhere in a React web application, for example in a calendar front end etc.
## Back end.

The back end is written in Python. 
- It serves the listing of available slots and reservation requests via a simple REST API.
- It connects to the Lightning Network LND node via gRPC to check whether a specific invoice has been paid. 
## Installation

In addition to the components included in this repository, an Umbrel node is used, which contains a Bitcoin full node as well as an LND Lightning node.