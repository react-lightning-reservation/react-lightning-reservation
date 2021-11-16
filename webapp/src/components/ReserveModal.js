import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import { Button, Modal } from 'react-bootstrap';

function ReserveModal(props) {
    console.log(props.slot)
    return  <Modal show={props.isOpen} onHide={() => props.setIsOpen(false)} size="xl">
                <Modal.Header closeButton>
                <Modal.Title>{props.slot.name}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    Instructor: {props.slot.instructor} <br/>
                    From: {props.slot.start} <br/>
                    Until: {props.slot.end} <br/>
                    Invoice: {props.slot.invoice} <br/>
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={() => props.setIsOpen(false)}>
                        Close
                    </Button>
                </Modal.Footer>
            </Modal>;
};

export default ReserveModal;