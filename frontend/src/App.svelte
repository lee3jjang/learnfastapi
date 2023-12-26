<script>
  let question_list = [];

  async function get_question_list() {
    const res = await fetch("http://localhost:8000/api/question/list");
    const json = await res.json();

    if (res.ok) {
      question_list = json;
    } else {
      alert("error");
    }
  }

  get_question_list();
</script>

{#await question_list}
  <p>...waiting</p>
{:then question_list}
  <ul>
    {#each question_list as { subject }}
      <li>{subject}</li>
    {/each}
  </ul>
{/await}
