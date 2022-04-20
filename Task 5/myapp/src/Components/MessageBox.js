import React, {useState} from "react"



export default function MessageBox(props){
    const [isEmpty, setIsEmpty] = useState(false);
    const [message, setMessage] = useState('');
    const [submitted, setSubmission] = useState(false);
    const handleMessage = (dataHere) =>{
        setMessage(dataHere.target.value);
        setSubmission(false);
    };
    const postMessage = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'msg':message})
    }

    const sendData = (data) => {
        data.preventDefault();
        if (message === '') {
            setIsEmpty(true);
            console.log("empty")
        } else {
            setSubmission(true);
            setIsEmpty(false);
            fetch('https://admin.remote.besic.org/api/statusmessage',postMessage)
                .then(response =>{
                    if(!response.ok){
                        throw new Error(`HTTP error: ${response.status}`);
                    }
                    console.log(response.text())
                    return response.text();
                });
        }
    };
    return (
        <div>
           <form>
               <label className="label">Message Box</label>
                   <input onChange={handleMessage} className="input" value={message} type="text"/>
                   <button onClick={sendData}>
                       Send Message
                   </button>
           </form>
        </div>
    );
}