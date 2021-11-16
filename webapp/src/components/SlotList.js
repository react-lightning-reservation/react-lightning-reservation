import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import { QueryClient, QueryClientProvider, useQuery } from "react-query";
import { ReactQueryDevtools } from "react-query/devtools";
import { Table, Button, Form, Col, InputGroup, FormControl, Card } from 'react-bootstrap';
import Slot from './Slot';

function SlotList(props) {
    const { isLoading, error, data, isFetching } = useQuery("repoData", () =>
        fetch(
        "http://localhost:8080/slots"
        ).then((res) => res.json())
    );
    
    if (isLoading) return "Loading...";
    
    if (error) return "An error has occurred: " + error.message;
    
    return (
        <div>
            <Table striped bordered hover>
                <thead><td>Event</td><td>Instructor</td><td>From</td><td>Until</td><td> </td></thead>
                <tbody>{data.slots.map((slot) => <Slot key={slot.id} slot={slot}/>)}</tbody>
            </Table>
            <div>{isFetching ? "Updating..." : ""}</div>
            <ReactQueryDevtools initialIsOpen />
        </div>
    );
}

export default SlotList;