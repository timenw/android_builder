package com.poem300.data.model

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "poems")
data class Poem(
    @PrimaryKey val id: Int,
    val title: String,           // 诗名（中文）
    val titlePinyin: String,     // 拼音
    val titleEn: String,         // 英文译名
    val author: String,          // 诗人（中文）
    val authorPinyin: String,    // 诗人拼音
    val authorEn: String,        // 诗人英文名
    val dynasty: String,         // 朝代
    val dynastyEn: String,       // 朝代英文
    val content: String,         // 原文（用\n分隔句）
    val translation: String,     // 英文翻译（用\n分隔）
    val annotation: String,      // 英文注释/赏析
    val category: String,        // 分类标签（英文逗号分隔）
    val difficulty: Int = 1      // 1=入门 2=进阶 3=深读
)

@Entity(tableName = "favorites")
data class Favorite(
    @PrimaryKey val poemId: Int,
    val note: String = "",       // 用户笔记
    val groupName: String = "Default", // 分组名
    val createdAt: Long = System.currentTimeMillis()
)
