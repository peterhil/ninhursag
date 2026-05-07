<script>
	let { controls } = $props()
</script>

<nav class="navigation">
	<section class="name">
		<h1>
			<a href="/mineral">Ninhursag</a>
		</h1>
		<a href="/about/">About</a>
	</section>
	<section class="controls">
		{@render controls()}
	</section>
</nav>
