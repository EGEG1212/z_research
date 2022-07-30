import { useState, useEffect} from 'react';

function App() {
    const [counter, setValue] = useState(0);
    const onClick = () => setValue((prev) => prev + 1);
    console.log("i run all the time")
    const iRunOnluOnce = () => {
        console.log("i run only once.");
    };
    useEffect(iRunOnluOnce, []);
  return (
    <div>
      <h1>{counter}</h1>
      <Button onClick={onClick}>click me</Button>
    </div>
  );
}

export default App;


