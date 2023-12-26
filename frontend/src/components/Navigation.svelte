<script>
  import { link } from "svelte-spa-router";
  import { is_login, username, page, access_token } from "../lib/store";
</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
  <div class="container-fluid">
    <a
      use:link
      class="navbar-brand"
      href="/"
      on:click={() => {
        $page = 0;
      }}>Pybo</a
    >
    <button
      type="button"
      class="navbar-toggler"
      data-bs-toggle="collapse"
      data-bs-target="#navbarSupportedContent"
    >
      <span class="navbar-toggler-icon" />
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        {#if $is_login}
          <li class="nav-item">
            <a
              use:link
              class="nav-link"
              href="/user-login"
              on:click={() => {
                $access_token = "";
                $username = "";
                $is_login = false;
              }}>로그아웃 ({$username})</a
            >
          </li>
        {:else}
          <li class="nav-item">
            <a use:link class="nav-link" href="/user-create">회원가입</a>
          </li>
          <li class="nav-item">
            <a use:link class="nav-link" href="/user-login">로그인</a>
          </li>
        {/if}
      </ul>
    </div>
  </div>
</nav>
