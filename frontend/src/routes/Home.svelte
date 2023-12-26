<script>
  import fastapi from "../lib/api";
  let question_list = [];

  function get_question_list() {
    fastapi("get", "/api/question/list", {}, (json) => {
      question_list = json;
    });
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
