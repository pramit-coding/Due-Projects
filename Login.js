import { useState } from "react";

function Login() {
    const [age, setAge] = useState("");
    const [message, setMessage] = useState("");

    const handleLogin = (e) => {
        e.preventDefault();
        if (Number(age) >= 18) {
            setMessage("Access granted");
        } else {
            setMessage("You must be 18 or older");
        }
    };

    return (
        <form onSubmit={handleLogin}>
            <input
                type="number"
                placeholder="Enter age"
                value={age}
                onChange={(e) => setAge(e.target.value)}
            />
            <button type="submit">Login</button>
            <p>{message}</p>
        </form>
    );
}

export default Login;

