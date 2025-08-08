# Exemple d’implémentation mémoire avec Langraph / Example of Memory Implementation with Langraph

## Description / Description

Ce projet présente une implémentation simple et fonctionnelle de la gestion de mémoire (checkpointing) avec Langraph.

Il illustre deux approches pour la persistance d’état dans un graphe Langraph :

- mémoire en local via `MemorySaver` (exemple simple, non persistant)
- persistance avec une base de données SQLite via `SqliteSaver`

L’exemple intègre également un chatbot utilisant le modèle GPT-4o-mini de Langchain-OpenAI, enrichi par des outils personnalisés.

This project demonstrates a simple and functional implementation of memory management (checkpointing) with Langraph.

It showcases two approaches for state persistence in a Langraph graph:

- Local memory using `MemorySaver` (simple example, non-persistent)
- Persistence with a SQLite database using `SqliteSaver`

The example also includes a chatbot using the GPT-4o-mini model from Langchain-OpenAI, enhanced with custom tools.

## Fonctionnalités / Features

- Gestion de l’état conversationnel avec `StateGraph` et typage strict via `TypedDict`
- Intégration d’un système de checkpoint compatible avec Langraph (nécessite les paramètres `thread_id`, `checkpoint_ns`, `checkpoint_id`)
- Persistance SQLite pour sauvegarder et recharger l’historique de conversation
- Interface utilisateur simple via Gradio pour tester le chatbot
- Chargement sécurisé des variables d’environnement avec `dotenv`

- Conversation state management with `StateGraph` and strict typing via `TypedDict`
- Integration of a checkpoint system compatible with Langraph (requires parameters: `thread_id`, `checkpoint_ns`, `checkpoint_id`)
- SQLite persistence to save and reload conversation history
- Simple user interface via Gradio to test the chatbot
- Secure environment variable loading with `dotenv`

## Installation

Make sure you have Python 3.9+ installed.

Install dependencies with:

```bash
uv sync install
```

Run the project:
```bash
uv run main.py
```
