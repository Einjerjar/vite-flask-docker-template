<script>
  import { API_ROOT } from '../config.js'
  let count = 0

  let data = {}

  const getData = async () => {
    console.log(`${API_ROOT}/api`)
    console.log(import.meta.env)
    const r = await fetch(`${API_ROOT}/api`)
    const j = await r.json()
    data = j
  }

  const increment = () => {
    count += 1
    getData()
  }
</script>

<button on:click={increment}>
  Click to fetch: {count}
</button>

{JSON.stringify(data)}

<style>
  button {
    font-family: inherit;
    font-size: inherit;
    padding: 1em 2em;
    color: #ff3e00;
    background-color: rgba(255, 62, 0, 0.1);
    border-radius: 2em;
    border: 2px solid rgba(255, 62, 0, 0);
    outline: none;
    width: 200px;
    font-variant-numeric: tabular-nums;
    cursor: pointer;
  }

  button:focus {
    border: 2px solid #ff3e00;
  }

  button:active {
    background-color: rgba(255, 62, 0, 0.2);
  }
</style>
