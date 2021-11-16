import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import { Button, Card } from 'react-bootstrap';
import ReserveModal from './ReserveModal';

function Slot(props) {
    const [modalIsOpen,setModalIsOpen] = useState(false);

    return (
        <tr>
            <td>{props.slot.name}</td>
            <td>{props.slot.instructor}</td>
            <td>{props.slot.start}</td>
            <td>{props.slot.end}</td>
            <td><Button variant='primary' onClick={()=>setModalIsOpen(true)}>Reserve</Button>
                <ReserveModal slot={props.slot} isOpen={modalIsOpen} setIsOpen={setModalIsOpen} />
            </td>
        </tr>
    );
}

export default Slot;