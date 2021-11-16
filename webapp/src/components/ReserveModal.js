import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import { Button, Modal } from 'react-bootstrap';
import QRious from "qrious";

function ReserveModal(props) {
    React.useEffect(() => {
        new QRious({
                element: document.getElementById("qr-div"),
                size: 300,
                value: props.slot.invoice
            });
    });

    return  <Modal show={props.isOpen} onHide={() => props.setIsOpen(false)} size="xl">
                <Modal.Header closeButton>
                <Modal.Title>{props.slot.name}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    Instructor: {props.slot.instructor} <br/>
                    From: {props.slot.start} <br/>
                    Until: {props.slot.end} <br/>
                    Invoice: {props.slot.invoice} <br/>
                    <canvas id="qr-div"/>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={() => props.setIsOpen(false)}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>;
};

export default ReserveModal;