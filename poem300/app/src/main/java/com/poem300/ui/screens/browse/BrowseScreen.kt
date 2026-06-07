package com.poem300.ui.screens.browse

import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.poem300.data.model.Poem
import com.poem300.ui.components.PoemCard
import com.poem300.ui.theme.*

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun BrowseScreen(
    poems: List<Poem>,
    authors: List<String>,
    dynasties: List<String>,
    favoriteIds: Set<Int>,
    onPoemClick: (Int) -> Unit,
    onFavoriteClick: (Int) -> Unit,
    onFilterByCategory: (String) -> Unit,
    onFilterByAuthor: (String) -> Unit,
    onFilterByDynasty: (String) -> Unit,
    onFilterByDifficulty: (Int) -> Unit,
    onBack: () -> Unit,
) {
    var selectedTab by remember { mutableIntStateOf(0) }
    val tabs = listOf("Theme", "Poet", "Dynasty", "Level")

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Browse") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Filled.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
        ) {
            TabRow(selectedTabIndex = selectedTab) {
                tabs.forEachIndexed { index, title ->
                    Tab(
                        selected = selectedTab == index,
                        onClick = { selectedTab = index },
                        text = { Text(title) }
                    )
                }
            }

            when (selectedTab) {
                0 -> ThemeFilterContent(poems, favoriteIds, onPoemClick, onFavoriteClick, onFilterByCategory)
                1 -> PoetFilterContent(poems, authors, favoriteIds, onPoemClick, onFavoriteClick, onFilterByAuthor)
                2 -> DynastyFilterContent(poems, dynasties, favoriteIds, onPoemClick, onFavoriteClick, onFilterByDynasty)
                3 -> DifficultyFilterContent(poems, favoriteIds, onPoemClick, onFavoriteClick, onFilterByDifficulty)
            }
        }
    }
}

@Composable
private fun ThemeFilterContent(
    poems: List<Poem>,
    favoriteIds: Set<Int>,
    onPoemClick: (Int) -> Unit,
    onFavoriteClick: (Int) -> Unit,
    onFilterByCategory: (String) -> Unit
) {
    val themes = listOf(
        "Nature" to "\uD83C\uDF3F", "Love" to "\u2764\uFE0F", "Moon" to "\uD83C\uDF19", "Mountain" to "\u26F0\uFE0F",
        "River" to "\uD83C\uDF0A", "Spring" to "\uD83C\uDF38", "Autumn" to "\uD83C\uDF42", "Winter" to "\u2744\uFE0F",
        "Farewell" to "\uD83D\uDC4B", "Friendship" to "\uD83E\uDD1D", "War" to "\u2694\uFE0F", "Homesickness" to "\uD83C\uDFE0",
        "Wine" to "\uD83C\uDF77", "Night" to "\uD83C\uDF19", "Philosophy" to "\uD83D\uDCAD", "History" to "\uD83D\uDCDC",
    )

    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        item {
            Text(
                text = "Choose a theme",
                style = MaterialTheme.typography.titleMedium,
                modifier = Modifier.padding(bottom = 8.dp)
            )
        }
        items(themes.chunked(2)) { row ->
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                row.forEach { (theme, emoji) ->
                    Card(
                        onClick = { onFilterByCategory(theme) },
                        modifier = Modifier
                            .weight(1f)
                            .height(72.dp),
                        shape = RoundedCornerShape(12.dp),
                        colors = CardDefaults.cardColors(
                            containerColor = MaterialTheme.colorScheme.surfaceVariant.copy(alpha = 0.4f)
                        )
                    ) {
                        Column(
                            modifier = Modifier
                                .fillMaxSize()
                                .padding(12.dp),
                            verticalArrangement = Arrangement.Center
                        ) {
                            Text(text = emoji, style = MaterialTheme.typography.titleMedium)
                            Text(
                                text = theme,
                                style = MaterialTheme.typography.labelLarge,
                                fontWeight = FontWeight.Medium
                            )
                        }
                    }
                }
                if (row.size == 1) Spacer(modifier = Modifier.weight(1f))
            }
        }
    }
}

@Composable
private fun PoetFilterContent(
    poems: List<Poem>,
    authors: List<String>,
    favoriteIds: Set<Int>,
    onPoemClick: (Int) -> Unit,
    onFavoriteClick: (Int) -> Unit,
    onFilterByAuthor: (String) -> Unit
) {
    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(4.dp)
    ) {
        item {
            Text(
                text = "Poets",
                style = MaterialTheme.typography.titleMedium,
                modifier = Modifier.padding(bottom = 8.dp)
            )
        }
        items(authors) { author ->
            val count = poems.count { it.author == author }
            ListItem(
                headlineContent = { Text(author) },
                supportingContent = { Text("$count poems") },
                leadingContent = {
                    Surface(
                        shape = RoundedCornerShape(8.dp),
                        color = MaterialTheme.colorScheme.primaryContainer,
                        modifier = Modifier.size(40.dp)
                    ) {
                        Box(contentAlignment = Alignment.Center) {
                            Text(
                                text = author.first().toString(),
                                style = MaterialTheme.typography.titleMedium,
                                color = MaterialTheme.colorScheme.onPrimaryContainer
                            )
                        }
                    }
                },
                trailingContent = {
                    Icon(Icons.Filled.ChevronRight, contentDescription = null)
                },
                modifier = Modifier.clickable(
                    indication = null,
                    interactionSource = remember { MutableInteractionSource() }
                ) { onFilterByAuthor(author) }
            )
        }
    }
}

@Composable
private fun DynastyFilterContent(
    poems: List<Poem>,
    dynasties: List<String>,
    favoriteIds: Set<Int>,
    onPoemClick: (Int) -> Unit,
    onFavoriteClick: (Int) -> Unit,
    onFilterByDynasty: (String) -> Unit
) {
    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(4.dp)
    ) {
        items(dynasties) { dynasty ->
            val count = poems.count { it.dynastyEn == dynasty }
            ListItem(
                headlineContent = { Text("$dynasty Dynasty") },
                supportingContent = { Text("$count poems") },
                trailingContent = {
                    Icon(Icons.Filled.ChevronRight, contentDescription = null)
                },
                modifier = Modifier.clickable(
                    indication = null,
                    interactionSource = remember { MutableInteractionSource() }
                ) { onFilterByDynasty(dynasty) }
            )
        }
    }
}

@Composable
private fun DifficultyFilterContent(
    poems: List<Poem>,
    favoriteIds: Set<Int>,
    onPoemClick: (Int) -> Unit,
    onFavoriteClick: (Int) -> Unit,
    onFilterByDifficulty: (Int) -> Unit
) {
    val levels = listOf(
        Triple(1, "Beginner", "Perfect for starting your journey"),
        Triple(2, "Intermediate", "Ready for deeper reading"),
        Triple(3, "Advanced", "For the dedicated reader"),
    )

    LazyColumn(
        contentPadding = PaddingValues(16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        items(levels) { (level, title, desc) ->
            val count = poems.count { it.difficulty == level }
            Card(
                onClick = { onFilterByDifficulty(level) },
                modifier = Modifier.fillMaxWidth(),
                shape = RoundedCornerShape(12.dp)
            ) {
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(16.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Surface(
                        shape = RoundedCornerShape(8.dp),
                        color = when (level) {
                            1 -> SageGreen
                            2 -> DustyBlue
                            else -> Terracotta
                        },
                        modifier = Modifier.size(48.dp)
                    ) {
                        Box(contentAlignment = Alignment.Center) {
                            Text(
                                text = level.toString(),
                                style = MaterialTheme.typography.titleLarge,
                                color = WarmWhite
                            )
                        }
                    }
                    Spacer(modifier = Modifier.width(16.dp))
                    Column(modifier = Modifier.weight(1f)) {
                        Text(text = title, style = MaterialTheme.typography.titleMedium)
                        Text(
                            text = desc,
                            style = MaterialTheme.typography.bodyMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant
                        )
                    }
                    Text(
                        text = "$count",
                        style = MaterialTheme.typography.titleMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant
                    )
                }
            }
        }
    }
}


