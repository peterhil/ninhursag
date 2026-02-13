<script lang="ts">
	import '$style/app.scss'
	import '$style/app.postcss'

	import Navbar from '$component/Navbar.svelte'
	import Alerts from '$component/Alerts.svelte'

	interface Props {
		children?: import('svelte').Snippet
	}

	let { children }: Props = $props()
</script>

<svelte:head>
	<title>Ninhursag</title>
</svelte:head>

<Alerts />
{@render children?.()}
