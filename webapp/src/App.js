import logo from './logo.svg';
import './App.css';
import SlotList from './components/SlotList';
import { QueryClient, QueryClientProvider, useQuery } from "react-query";

const queryClient = new QueryClient();

function App() {
  return (
    <div>
      <header><h1>Reservations:</h1></header>
      <body>
        <p>
          <QueryClientProvider client={queryClient}>
            <SlotList/>
          </QueryClientProvider>  
        </p>
      </body>
    </div>
  );
}

export default App;
