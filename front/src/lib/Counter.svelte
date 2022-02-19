<script>
  let count = 0

  let data = {}

  const getData = async () => {
    const r = await fetch('http://host.docker.internal:5001/')
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
