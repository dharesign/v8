#!/usr/bin/env python3
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
# yapf: disable

INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  96: "SHARED_STRING_TYPE",
  98: "SHARED_EXTERNAL_STRING_TYPE",
  101: "SHARED_THIN_STRING_TYPE",
  104: "SHARED_ONE_BYTE_STRING_TYPE",
  106: "SHARED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  109: "SHARED_THIN_ONE_BYTE_STRING_TYPE",
  114: "SHARED_UNCACHED_EXTERNAL_STRING_TYPE",
  122: "SHARED_UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  128: "SYMBOL_TYPE",
  129: "BIG_INT_BASE_TYPE",
  130: "HEAP_NUMBER_TYPE",
  131: "ODDBALL_TYPE",
  132: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  133: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  134: "CALLABLE_TASK_TYPE",
  135: "CALLBACK_TASK_TYPE",
  136: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  137: "LOAD_HANDLER_TYPE",
  138: "STORE_HANDLER_TYPE",
  139: "FUNCTION_TEMPLATE_INFO_TYPE",
  140: "OBJECT_TEMPLATE_INFO_TYPE",
  141: "ACCESS_CHECK_INFO_TYPE",
  142: "ACCESSOR_PAIR_TYPE",
  143: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  144: "ALLOCATION_MEMENTO_TYPE",
  145: "ALLOCATION_SITE_TYPE",
  146: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  147: "ASM_WASM_DATA_TYPE",
  148: "ASYNC_GENERATOR_REQUEST_TYPE",
  149: "BREAK_POINT_TYPE",
  150: "BREAK_POINT_INFO_TYPE",
  151: "CALL_SITE_INFO_TYPE",
  152: "CLASS_POSITIONS_TYPE",
  153: "DEBUG_INFO_TYPE",
  154: "ENUM_CACHE_TYPE",
  155: "ERROR_STACK_DATA_TYPE",
  156: "FEEDBACK_CELL_TYPE",
  157: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  158: "INTERCEPTOR_INFO_TYPE",
  159: "INTERPRETER_DATA_TYPE",
  160: "MODULE_REQUEST_TYPE",
  161: "PROMISE_CAPABILITY_TYPE",
  162: "PROMISE_ON_STACK_TYPE",
  163: "PROMISE_REACTION_TYPE",
  164: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  165: "PROTOTYPE_INFO_TYPE",
  166: "REG_EXP_BOILERPLATE_DESCRIPTION_TYPE",
  167: "SCRIPT_TYPE",
  168: "SCRIPT_OR_MODULE_TYPE",
  169: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  170: "STACK_FRAME_INFO_TYPE",
  171: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  172: "TUPLE2_TYPE",
  173: "WASM_EXCEPTION_TAG_TYPE",
  174: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  175: "FIXED_ARRAY_TYPE",
  176: "HASH_TABLE_TYPE",
  177: "EPHEMERON_HASH_TABLE_TYPE",
  178: "GLOBAL_DICTIONARY_TYPE",
  179: "NAME_DICTIONARY_TYPE",
  180: "NAME_TO_INDEX_HASH_TABLE_TYPE",
  181: "NUMBER_DICTIONARY_TYPE",
  182: "ORDERED_HASH_MAP_TYPE",
  183: "ORDERED_HASH_SET_TYPE",
  184: "ORDERED_NAME_DICTIONARY_TYPE",
  185: "REGISTERED_SYMBOL_TABLE_TYPE",
  186: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  187: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  188: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  189: "SCRIPT_CONTEXT_TABLE_TYPE",
  190: "BYTE_ARRAY_TYPE",
  191: "BYTECODE_ARRAY_TYPE",
  192: "FIXED_DOUBLE_ARRAY_TYPE",
  193: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  194: "SLOPPY_ARGUMENTS_ELEMENTS_TYPE",
  195: "TURBOSHAFT_FLOAT64_TYPE_TYPE",
  196: "TURBOSHAFT_FLOAT64_RANGE_TYPE_TYPE",
  197: "TURBOSHAFT_FLOAT64_SET_TYPE_TYPE",
  198: "TURBOSHAFT_WORD32_TYPE_TYPE",
  199: "TURBOSHAFT_WORD32_RANGE_TYPE_TYPE",
  200: "TURBOSHAFT_WORD32_SET_TYPE_TYPE",
  201: "TURBOSHAFT_WORD64_TYPE_TYPE",
  202: "TURBOSHAFT_WORD64_RANGE_TYPE_TYPE",
  203: "TURBOSHAFT_WORD64_SET_TYPE_TYPE",
  204: "FOREIGN_TYPE",
  205: "AWAIT_CONTEXT_TYPE",
  206: "BLOCK_CONTEXT_TYPE",
  207: "CATCH_CONTEXT_TYPE",
  208: "DEBUG_EVALUATE_CONTEXT_TYPE",
  209: "EVAL_CONTEXT_TYPE",
  210: "FUNCTION_CONTEXT_TYPE",
  211: "MODULE_CONTEXT_TYPE",
  212: "NATIVE_CONTEXT_TYPE",
  213: "SCRIPT_CONTEXT_TYPE",
  214: "WITH_CONTEXT_TYPE",
  215: "TURBOFAN_BITSET_TYPE_TYPE",
  216: "TURBOFAN_HEAP_CONSTANT_TYPE_TYPE",
  217: "TURBOFAN_OTHER_NUMBER_CONSTANT_TYPE_TYPE",
  218: "TURBOFAN_RANGE_TYPE_TYPE",
  219: "TURBOFAN_UNION_TYPE_TYPE",
  220: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  221: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_AND_JOB_TYPE",
  222: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  223: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_WITH_JOB_TYPE",
  224: "WASM_FUNCTION_DATA_TYPE",
  225: "WASM_CAPI_FUNCTION_DATA_TYPE",
  226: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  227: "WASM_JS_FUNCTION_DATA_TYPE",
  228: "EXPORTED_SUB_CLASS_BASE_TYPE",
  229: "EXPORTED_SUB_CLASS_TYPE",
  230: "EXPORTED_SUB_CLASS2_TYPE",
  231: "SMALL_ORDERED_HASH_MAP_TYPE",
  232: "SMALL_ORDERED_HASH_SET_TYPE",
  233: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  234: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  235: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  236: "DESCRIPTOR_ARRAY_TYPE",
  237: "STRONG_DESCRIPTOR_ARRAY_TYPE",
  238: "SOURCE_TEXT_MODULE_TYPE",
  239: "SYNTHETIC_MODULE_TYPE",
  240: "WEAK_FIXED_ARRAY_TYPE",
  241: "TRANSITION_ARRAY_TYPE",
  242: "ACCESSOR_INFO_TYPE",
  243: "CALL_HANDLER_INFO_TYPE",
  244: "CELL_TYPE",
  245: "CODE_TYPE",
  246: "COVERAGE_INFO_TYPE",
  247: "EMBEDDER_DATA_ARRAY_TYPE",
  248: "FEEDBACK_METADATA_TYPE",
  249: "FEEDBACK_VECTOR_TYPE",
  250: "FILLER_TYPE",
  251: "FREE_SPACE_TYPE",
  252: "INSTRUCTION_STREAM_TYPE",
  253: "INTERNAL_CLASS_TYPE",
  254: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  255: "MAP_TYPE",
  256: "MEGA_DOM_HANDLER_TYPE",
  257: "ON_HEAP_BASIC_BLOCK_PROFILER_DATA_TYPE",
  258: "PREPARSE_DATA_TYPE",
  259: "PROPERTY_ARRAY_TYPE",
  260: "PROPERTY_CELL_TYPE",
  261: "SCOPE_INFO_TYPE",
  262: "SHARED_FUNCTION_INFO_TYPE",
  263: "SMI_BOX_TYPE",
  264: "SMI_PAIR_TYPE",
  265: "SORT_STATE_TYPE",
  266: "SWISS_NAME_DICTIONARY_TYPE",
  267: "WASM_API_FUNCTION_REF_TYPE",
  268: "WASM_CONTINUATION_OBJECT_TYPE",
  269: "WASM_INTERNAL_FUNCTION_TYPE",
  270: "WASM_RESUME_DATA_TYPE",
  271: "WASM_STRING_VIEW_ITER_TYPE",
  272: "WASM_TYPE_INFO_TYPE",
  273: "WEAK_ARRAY_LIST_TYPE",
  274: "WEAK_CELL_TYPE",
  275: "WASM_ARRAY_TYPE",
  276: "WASM_STRUCT_TYPE",
  277: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  278: "JS_GLOBAL_OBJECT_TYPE",
  279: "JS_GLOBAL_PROXY_TYPE",
  280: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1058: "JS_API_OBJECT_TYPE",
  2058: "JS_LAST_DUMMY_API_OBJECT_TYPE",
  2059: "JS_DATA_VIEW_TYPE",
  2060: "JS_TYPED_ARRAY_TYPE",
  2061: "JS_ARRAY_BUFFER_TYPE",
  2062: "JS_PROMISE_TYPE",
  2063: "JS_BOUND_FUNCTION_TYPE",
  2064: "JS_WRAPPED_FUNCTION_TYPE",
  2065: "JS_FUNCTION_TYPE",
  2066: "BIGINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2067: "BIGUINT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2068: "FLOAT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2069: "FLOAT64_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2070: "INT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2071: "INT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2072: "INT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2073: "UINT16_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2074: "UINT32_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2075: "UINT8_CLAMPED_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2076: "UINT8_TYPED_ARRAY_CONSTRUCTOR_TYPE",
  2077: "JS_ARRAY_CONSTRUCTOR_TYPE",
  2078: "JS_PROMISE_CONSTRUCTOR_TYPE",
  2079: "JS_REG_EXP_CONSTRUCTOR_TYPE",
  2080: "JS_CLASS_CONSTRUCTOR_TYPE",
  2081: "JS_ARRAY_ITERATOR_PROTOTYPE_TYPE",
  2082: "JS_ITERATOR_PROTOTYPE_TYPE",
  2083: "JS_MAP_ITERATOR_PROTOTYPE_TYPE",
  2084: "JS_OBJECT_PROTOTYPE_TYPE",
  2085: "JS_PROMISE_PROTOTYPE_TYPE",
  2086: "JS_REG_EXP_PROTOTYPE_TYPE",
  2087: "JS_SET_ITERATOR_PROTOTYPE_TYPE",
  2088: "JS_SET_PROTOTYPE_TYPE",
  2089: "JS_STRING_ITERATOR_PROTOTYPE_TYPE",
  2090: "JS_TYPED_ARRAY_PROTOTYPE_TYPE",
  2091: "JS_MAP_KEY_ITERATOR_TYPE",
  2092: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  2093: "JS_MAP_VALUE_ITERATOR_TYPE",
  2094: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  2095: "JS_SET_VALUE_ITERATOR_TYPE",
  2096: "JS_GENERATOR_OBJECT_TYPE",
  2097: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  2098: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  2099: "JS_MAP_TYPE",
  2100: "JS_SET_TYPE",
  2101: "JS_WEAK_MAP_TYPE",
  2102: "JS_WEAK_SET_TYPE",
  2103: "JS_ARGUMENTS_OBJECT_TYPE",
  2104: "JS_ARRAY_TYPE",
  2105: "JS_ARRAY_ITERATOR_TYPE",
  2106: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  2107: "JS_COLLATOR_TYPE",
  2108: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  2109: "JS_DATE_TYPE",
  2110: "JS_DATE_TIME_FORMAT_TYPE",
  2111: "JS_DISPLAY_NAMES_TYPE",
  2112: "JS_DURATION_FORMAT_TYPE",
  2113: "JS_ERROR_TYPE",
  2114: "JS_EXTERNAL_OBJECT_TYPE",
  2115: "JS_FINALIZATION_REGISTRY_TYPE",
  2116: "JS_LIST_FORMAT_TYPE",
  2117: "JS_LOCALE_TYPE",
  2118: "JS_MESSAGE_OBJECT_TYPE",
  2119: "JS_NUMBER_FORMAT_TYPE",
  2120: "JS_PLURAL_RULES_TYPE",
  2121: "JS_RAW_JSON_TYPE",
  2122: "JS_REG_EXP_TYPE",
  2123: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  2124: "JS_RELATIVE_TIME_FORMAT_TYPE",
  2125: "JS_SEGMENT_ITERATOR_TYPE",
  2126: "JS_SEGMENTER_TYPE",
  2127: "JS_SEGMENTS_TYPE",
  2128: "JS_SHADOW_REALM_TYPE",
  2129: "JS_STRING_ITERATOR_TYPE",
  2130: "JS_TEMPORAL_CALENDAR_TYPE",
  2131: "JS_TEMPORAL_DURATION_TYPE",
  2132: "JS_TEMPORAL_INSTANT_TYPE",
  2133: "JS_TEMPORAL_PLAIN_DATE_TYPE",
  2134: "JS_TEMPORAL_PLAIN_DATE_TIME_TYPE",
  2135: "JS_TEMPORAL_PLAIN_MONTH_DAY_TYPE",
  2136: "JS_TEMPORAL_PLAIN_TIME_TYPE",
  2137: "JS_TEMPORAL_PLAIN_YEAR_MONTH_TYPE",
  2138: "JS_TEMPORAL_TIME_ZONE_TYPE",
  2139: "JS_TEMPORAL_ZONED_DATE_TIME_TYPE",
  2140: "JS_V8_BREAK_ITERATOR_TYPE",
  2141: "JS_WEAK_REF_TYPE",
  2142: "WASM_EXCEPTION_PACKAGE_TYPE",
  2143: "WASM_GLOBAL_OBJECT_TYPE",
  2144: "WASM_INSTANCE_OBJECT_TYPE",
  2145: "WASM_MEMORY_OBJECT_TYPE",
  2146: "WASM_MODULE_OBJECT_TYPE",
  2147: "WASM_SUSPENDER_OBJECT_TYPE",
  2148: "WASM_TABLE_OBJECT_TYPE",
  2149: "WASM_TAG_OBJECT_TYPE",
  2150: "WASM_VALUE_OBJECT_TYPE",
  2151: "JS_ATOMICS_CONDITION_TYPE",
  2152: "JS_ATOMICS_MUTEX_TYPE",
  2153: "JS_SHARED_ARRAY_TYPE",
  2154: "JS_SHARED_STRUCT_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
    ("read_only_space", 0x02141): (255, "MetaMap"),
    ("read_only_space", 0x02169): (175, "FixedArrayMap"),
    ("read_only_space", 0x02191): (240, "WeakFixedArrayMap"),
    ("read_only_space", 0x021b9): (273, "WeakArrayListMap"),
    ("read_only_space", 0x021e1): (175, "FixedCOWArrayMap"),
    ("read_only_space", 0x02209): (236, "DescriptorArrayMap"),
    ("read_only_space", 0x02231): (131, "UndefinedMap"),
    ("read_only_space", 0x02259): (131, "NullMap"),
    ("read_only_space", 0x02281): (131, "TheHoleMap"),
    ("read_only_space", 0x02319): (132, "PromiseFulfillReactionJobTaskMap"),
    ("read_only_space", 0x02341): (133, "PromiseRejectReactionJobTaskMap"),
    ("read_only_space", 0x02369): (134, "CallableTaskMap"),
    ("read_only_space", 0x02391): (135, "CallbackTaskMap"),
    ("read_only_space", 0x023b9): (136, "PromiseResolveThenableJobTaskMap"),
    ("read_only_space", 0x023e1): (139, "FunctionTemplateInfoMap"),
    ("read_only_space", 0x02409): (140, "ObjectTemplateInfoMap"),
    ("read_only_space", 0x02431): (141, "AccessCheckInfoMap"),
    ("read_only_space", 0x02459): (142, "AccessorPairMap"),
    ("read_only_space", 0x02481): (143, "AliasedArgumentsEntryMap"),
    ("read_only_space", 0x024a9): (144, "AllocationMementoMap"),
    ("read_only_space", 0x024d1): (146, "ArrayBoilerplateDescriptionMap"),
    ("read_only_space", 0x024f9): (147, "AsmWasmDataMap"),
    ("read_only_space", 0x02521): (148, "AsyncGeneratorRequestMap"),
    ("read_only_space", 0x02549): (149, "BreakPointMap"),
    ("read_only_space", 0x02571): (150, "BreakPointInfoMap"),
    ("read_only_space", 0x02599): (151, "CallSiteInfoMap"),
    ("read_only_space", 0x025c1): (152, "ClassPositionsMap"),
    ("read_only_space", 0x025e9): (153, "DebugInfoMap"),
    ("read_only_space", 0x02611): (154, "EnumCacheMap"),
    ("read_only_space", 0x02639): (155, "ErrorStackDataMap"),
    ("read_only_space", 0x02661): (157, "FunctionTemplateRareDataMap"),
    ("read_only_space", 0x02689): (158, "InterceptorInfoMap"),
    ("read_only_space", 0x026b1): (159, "InterpreterDataMap"),
    ("read_only_space", 0x026d9): (160, "ModuleRequestMap"),
    ("read_only_space", 0x02701): (161, "PromiseCapabilityMap"),
    ("read_only_space", 0x02729): (162, "PromiseOnStackMap"),
    ("read_only_space", 0x02751): (163, "PromiseReactionMap"),
    ("read_only_space", 0x02779): (164, "PropertyDescriptorObjectMap"),
    ("read_only_space", 0x027a1): (165, "PrototypeInfoMap"),
    ("read_only_space", 0x027c9): (166, "RegExpBoilerplateDescriptionMap"),
    ("read_only_space", 0x027f1): (167, "ScriptMap"),
    ("read_only_space", 0x02819): (168, "ScriptOrModuleMap"),
    ("read_only_space", 0x02841): (169, "SourceTextModuleInfoEntryMap"),
    ("read_only_space", 0x02869): (170, "StackFrameInfoMap"),
    ("read_only_space", 0x02891): (171, "TemplateObjectDescriptionMap"),
    ("read_only_space", 0x028b9): (172, "Tuple2Map"),
    ("read_only_space", 0x028e1): (173, "WasmExceptionTagMap"),
    ("read_only_space", 0x02909): (174, "WasmIndirectFunctionTableMap"),
    ("read_only_space", 0x02931): (145, "AllocationSiteWithWeakNextMap"),
    ("read_only_space", 0x02959): (145, "AllocationSiteWithoutWeakNextMap"),
    ("read_only_space", 0x02981): (137, "LoadHandler1Map"),
    ("read_only_space", 0x029a9): (137, "LoadHandler2Map"),
    ("read_only_space", 0x029d1): (137, "LoadHandler3Map"),
    ("read_only_space", 0x029f9): (138, "StoreHandler0Map"),
    ("read_only_space", 0x02a21): (138, "StoreHandler1Map"),
    ("read_only_space", 0x02a49): (138, "StoreHandler2Map"),
    ("read_only_space", 0x02a71): (138, "StoreHandler3Map"),
    ("read_only_space", 0x02ab5): (261, "ScopeInfoMap"),
    ("read_only_space", 0x02add): (175, "ModuleInfoMap"),
    ("read_only_space", 0x02b05): (187, "ClosureFeedbackCellArrayMap"),
    ("read_only_space", 0x02b2d): (249, "FeedbackVectorMap"),
    ("read_only_space", 0x02b55): (130, "HeapNumberMap"),
    ("read_only_space", 0x02b7d): (128, "SymbolMap"),
    ("read_only_space", 0x02ba5): (204, "ForeignMap"),
    ("read_only_space", 0x02bcd): (256, "MegaDomHandlerMap"),
    ("read_only_space", 0x02bf5): (131, "BooleanMap"),
    ("read_only_space", 0x02c1d): (131, "UninitializedMap"),
    ("read_only_space", 0x02c45): (131, "ArgumentsMarkerMap"),
    ("read_only_space", 0x02c6d): (131, "ExceptionMap"),
    ("read_only_space", 0x02c95): (131, "TerminationExceptionMap"),
    ("read_only_space", 0x02cbd): (131, "OptimizedOutMap"),
    ("read_only_space", 0x02ce5): (131, "StaleRegisterMap"),
    ("read_only_space", 0x02d0d): (131, "SelfReferenceMarkerMap"),
    ("read_only_space", 0x02d35): (131, "BasicBlockCountersMarkerMap"),
    ("read_only_space", 0x02d5d): (129, "BigIntMap"),
    ("read_only_space", 0x02d85): (32, "StringMap"),
    ("read_only_space", 0x02dad): (40, "OneByteStringMap"),
    ("read_only_space", 0x02dd5): (33, "ConsStringMap"),
    ("read_only_space", 0x02dfd): (41, "ConsOneByteStringMap"),
    ("read_only_space", 0x02e25): (35, "SlicedStringMap"),
    ("read_only_space", 0x02e4d): (43, "SlicedOneByteStringMap"),
    ("read_only_space", 0x02e75): (34, "ExternalStringMap"),
    ("read_only_space", 0x02e9d): (42, "ExternalOneByteStringMap"),
    ("read_only_space", 0x02ec5): (50, "UncachedExternalStringMap"),
    ("read_only_space", 0x02eed): (58, "UncachedExternalOneByteStringMap"),
    ("read_only_space", 0x02f15): (0, "InternalizedStringMap"),
    ("read_only_space", 0x02f3d): (8, "OneByteInternalizedStringMap"),
    ("read_only_space", 0x02f65): (2, "ExternalInternalizedStringMap"),
    ("read_only_space", 0x02f8d): (10, "ExternalOneByteInternalizedStringMap"),
    ("read_only_space", 0x02fb5): (18, "UncachedExternalInternalizedStringMap"),
    ("read_only_space", 0x02fdd): (26, "UncachedExternalOneByteInternalizedStringMap"),
    ("read_only_space", 0x03005): (37, "ThinStringMap"),
    ("read_only_space", 0x0302d): (45, "ThinOneByteStringMap"),
    ("read_only_space", 0x03055): (96, "SharedStringMap"),
    ("read_only_space", 0x0307d): (104, "SharedOneByteStringMap"),
    ("read_only_space", 0x030a5): (98, "SharedExternalStringMap"),
    ("read_only_space", 0x030cd): (106, "SharedExternalOneByteStringMap"),
    ("read_only_space", 0x030f5): (114, "SharedUncachedExternalStringMap"),
    ("read_only_space", 0x0311d): (122, "SharedUncachedExternalOneByteStringMap"),
    ("read_only_space", 0x03145): (101, "SharedThinStringMap"),
    ("read_only_space", 0x0316d): (109, "SharedThinOneByteStringMap"),
    ("read_only_space", 0x03195): (192, "FixedDoubleArrayMap"),
    ("read_only_space", 0x031bd): (248, "FeedbackMetadataArrayMap"),
    ("read_only_space", 0x031e5): (190, "ByteArrayMap"),
    ("read_only_space", 0x0320d): (191, "BytecodeArrayMap"),
    ("read_only_space", 0x03235): (251, "FreeSpaceMap"),
    ("read_only_space", 0x0325d): (259, "PropertyArrayMap"),
    ("read_only_space", 0x03285): (231, "SmallOrderedHashMapMap"),
    ("read_only_space", 0x032ad): (232, "SmallOrderedHashSetMap"),
    ("read_only_space", 0x032d5): (233, "SmallOrderedNameDictionaryMap"),
    ("read_only_space", 0x032fd): (222, "UncompiledDataWithoutPreparseDataMap"),
    ("read_only_space", 0x03325): (220, "UncompiledDataWithPreparseDataMap"),
    ("read_only_space", 0x0334d): (223, "UncompiledDataWithoutPreparseDataWithJobMap"),
    ("read_only_space", 0x03375): (221, "UncompiledDataWithPreparseDataAndJobMap"),
    ("read_only_space", 0x0339d): (257, "OnHeapBasicBlockProfilerDataMap"),
    ("read_only_space", 0x033c5): (215, "TurbofanBitsetTypeMap"),
    ("read_only_space", 0x033ed): (219, "TurbofanUnionTypeMap"),
    ("read_only_space", 0x03415): (218, "TurbofanRangeTypeMap"),
    ("read_only_space", 0x0343d): (216, "TurbofanHeapConstantTypeMap"),
    ("read_only_space", 0x03465): (217, "TurbofanOtherNumberConstantTypeMap"),
    ("read_only_space", 0x0348d): (198, "TurboshaftWord32TypeMap"),
    ("read_only_space", 0x034b5): (199, "TurboshaftWord32RangeTypeMap"),
    ("read_only_space", 0x034dd): (201, "TurboshaftWord64TypeMap"),
    ("read_only_space", 0x03505): (202, "TurboshaftWord64RangeTypeMap"),
    ("read_only_space", 0x0352d): (195, "TurboshaftFloat64TypeMap"),
    ("read_only_space", 0x03555): (196, "TurboshaftFloat64RangeTypeMap"),
    ("read_only_space", 0x0357d): (253, "InternalClassMap"),
    ("read_only_space", 0x035a5): (264, "SmiPairMap"),
    ("read_only_space", 0x035cd): (263, "SmiBoxMap"),
    ("read_only_space", 0x035f5): (228, "ExportedSubClassBaseMap"),
    ("read_only_space", 0x0361d): (229, "ExportedSubClassMap"),
    ("read_only_space", 0x03645): (234, "AbstractInternalClassSubclass1Map"),
    ("read_only_space", 0x0366d): (235, "AbstractInternalClassSubclass2Map"),
    ("read_only_space", 0x03695): (230, "ExportedSubClass2Map"),
    ("read_only_space", 0x036bd): (265, "SortStateMap"),
    ("read_only_space", 0x036e5): (271, "WasmStringViewIterMap"),
    ("read_only_space", 0x0370d): (194, "SloppyArgumentsElementsMap"),
    ("read_only_space", 0x03735): (237, "StrongDescriptorArrayMap"),
    ("read_only_space", 0x0375d): (200, "TurboshaftWord32SetTypeMap"),
    ("read_only_space", 0x03785): (203, "TurboshaftWord64SetTypeMap"),
    ("read_only_space", 0x037ad): (197, "TurboshaftFloat64SetTypeMap"),
    ("read_only_space", 0x037d5): (193, "InternalClassWithSmiElementsMap"),
    ("read_only_space", 0x037fd): (254, "InternalClassWithStructElementsMap"),
    ("read_only_space", 0x03825): (252, "InstructionStreamMap"),
    ("read_only_space", 0x0384d): (244, "CellMap"),
    ("read_only_space", 0x0387d): (260, "GlobalPropertyCellMap"),
    ("read_only_space", 0x038a5): (250, "OnePointerFillerMap"),
    ("read_only_space", 0x038cd): (250, "TwoPointerFillerMap"),
    ("read_only_space", 0x038f5): (156, "NoClosuresCellMap"),
    ("read_only_space", 0x0391d): (156, "OneClosureCellMap"),
    ("read_only_space", 0x03945): (156, "ManyClosuresCellMap"),
    ("read_only_space", 0x0396d): (241, "TransitionArrayMap"),
    ("read_only_space", 0x03995): (176, "HashTableMap"),
    ("read_only_space", 0x039bd): (182, "OrderedHashMapMap"),
    ("read_only_space", 0x039e5): (183, "OrderedHashSetMap"),
    ("read_only_space", 0x03a0d): (184, "OrderedNameDictionaryMap"),
    ("read_only_space", 0x03a35): (179, "NameDictionaryMap"),
    ("read_only_space", 0x03a5d): (266, "SwissNameDictionaryMap"),
    ("read_only_space", 0x03a85): (178, "GlobalDictionaryMap"),
    ("read_only_space", 0x03aad): (181, "NumberDictionaryMap"),
    ("read_only_space", 0x03ad5): (186, "SimpleNumberDictionaryMap"),
    ("read_only_space", 0x03afd): (180, "NameToIndexHashTableMap"),
    ("read_only_space", 0x03b25): (185, "RegisteredSymbolTableMap"),
    ("read_only_space", 0x03b4d): (247, "EmbedderDataArrayMap"),
    ("read_only_space", 0x03b75): (177, "EphemeronHashTableMap"),
    ("read_only_space", 0x03b9d): (175, "ArrayListMap"),
    ("read_only_space", 0x03bc5): (189, "ScriptContextTableMap"),
    ("read_only_space", 0x03bed): (188, "ObjectBoilerplateDescriptionMap"),
    ("read_only_space", 0x03c15): (246, "CoverageInfoMap"),
    ("read_only_space", 0x03c3d): (242, "AccessorInfoMap"),
    ("read_only_space", 0x03c65): (243, "SideEffectCallHandlerInfoMap"),
    ("read_only_space", 0x03c8d): (243, "SideEffectFreeCallHandlerInfoMap"),
    ("read_only_space", 0x03cb5): (243, "NextCallSideEffectFreeCallHandlerInfoMap"),
    ("read_only_space", 0x03cdd): (258, "PreparseDataMap"),
    ("read_only_space", 0x03d05): (262, "SharedFunctionInfoMap"),
    ("read_only_space", 0x03d2d): (238, "SourceTextModuleMap"),
    ("read_only_space", 0x03d55): (239, "SyntheticModuleMap"),
    ("read_only_space", 0x03d7d): (245, "CodeMap"),
    ("read_only_space", 0x03da5): (267, "WasmApiFunctionRefMap"),
    ("read_only_space", 0x03dcd): (225, "WasmCapiFunctionDataMap"),
    ("read_only_space", 0x03df5): (226, "WasmExportedFunctionDataMap"),
    ("read_only_space", 0x03e1d): (269, "WasmInternalFunctionMap"),
    ("read_only_space", 0x03e45): (227, "WasmJSFunctionDataMap"),
    ("read_only_space", 0x03e6d): (270, "WasmResumeDataMap"),
    ("read_only_space", 0x03e95): (272, "WasmTypeInfoMap"),
    ("read_only_space", 0x03ebd): (268, "WasmContinuationObjectMap"),
    ("read_only_space", 0x03ee5): (274, "WeakCellMap"),
    ("old_space", 0x043bd): (2114, "ExternalMap"),
    ("old_space", 0x043e5): (2118, "JSMessageObjectMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x022a9): "EmptyFixedArray",
  ("read_only_space", 0x022b1): "EmptyWeakFixedArray",
  ("read_only_space", 0x022b9): "EmptyWeakArrayList",
  ("read_only_space", 0x022c5): "NullValue",
  ("read_only_space", 0x022e1): "UndefinedValue",
  ("read_only_space", 0x022fd): "TheHoleValue",
  ("read_only_space", 0x02a99): "EmptyEnumCache",
  ("read_only_space", 0x02aa5): "EmptyDescriptorArray",
  ("read_only_space", 0x03875): "InvalidPrototypeValidityCell",
  ("read_only_space", 0x03f0d): "EmptyArrayList",
  ("read_only_space", 0x03f19): "EmptyScopeInfo",
  ("read_only_space", 0x03f29): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x03f35): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x03f41): "TrueValue",
  ("read_only_space", 0x03f5d): "FalseValue",
  ("read_only_space", 0x03f79): "EmptyByteArray",
  ("read_only_space", 0x03f81): "EmptyPropertyArray",
  ("read_only_space", 0x03f89): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x03f91): "NoOpInterceptorInfo",
  ("read_only_space", 0x03fb9): "MinusZeroValue",
  ("read_only_space", 0x03fc5): "NanValue",
  ("read_only_space", 0x03fd1): "HoleNanValue",
  ("read_only_space", 0x03fdd): "InfinityValue",
  ("read_only_space", 0x03fe9): "MinusInfinityValue",
  ("read_only_space", 0x03ff5): "MaxSafeInteger",
  ("read_only_space", 0x04001): "MaxUInt32",
  ("read_only_space", 0x0400d): "SmiMinValue",
  ("read_only_space", 0x04019): "SmiMaxValuePlusOne",
  ("read_only_space", 0x04025): "HashSeed",
  ("read_only_space", 0x04035): "SingleCharacterStringTable",
  ("read_only_space", 0x0543d): "empty_string",
  ("read_only_space", 0x07b35): "UninitializedValue",
  ("read_only_space", 0x07b6d): "ArgumentsMarker",
  ("read_only_space", 0x07ba5): "TerminationException",
  ("read_only_space", 0x07be5): "Exception",
  ("read_only_space", 0x07c01): "OptimizedOut",
  ("read_only_space", 0x07c39): "StaleRegister",
  ("read_only_space", 0x07c71): "SelfReferenceMarker",
  ("read_only_space", 0x07cb1): "BasicBlockCountersMarker",
  ("read_only_space", 0x081c9): "EmptyPropertyDictionary",
  ("read_only_space", 0x081f1): "EmptySymbolTable",
  ("read_only_space", 0x0820d): "EmptySlowElementDictionary",
  ("read_only_space", 0x08231): "EmptyOrderedHashMap",
  ("read_only_space", 0x08245): "EmptyOrderedHashSet",
  ("read_only_space", 0x08259): "EmptyOrderedPropertyDictionary",
  ("read_only_space", 0x0827d): "EmptySwissPropertyDictionary",
  ("read_only_space", 0x0829d): "EmptyFeedbackMetadata",
  ("read_only_space", 0x082a9): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x082c9): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x082ed): "NativeScopeInfo",
  ("read_only_space", 0x08305): "ShadowRealmScopeInfo",
  ("old_space", 0x0426d): "ArgumentsIteratorAccessor",
  ("old_space", 0x04285): "ArrayLengthAccessor",
  ("old_space", 0x0429d): "BoundFunctionLengthAccessor",
  ("old_space", 0x042b5): "BoundFunctionNameAccessor",
  ("old_space", 0x042cd): "ErrorStackAccessor",
  ("old_space", 0x042e5): "FunctionArgumentsAccessor",
  ("old_space", 0x042fd): "FunctionCallerAccessor",
  ("old_space", 0x04315): "FunctionNameAccessor",
  ("old_space", 0x0432d): "FunctionLengthAccessor",
  ("old_space", 0x04345): "FunctionPrototypeAccessor",
  ("old_space", 0x0435d): "StringLengthAccessor",
  ("old_space", 0x04375): "ValueUnavailableAccessor",
  ("old_space", 0x0438d): "WrappedFunctionLengthAccessor",
  ("old_space", 0x043a5): "WrappedFunctionNameAccessor",
  ("old_space", 0x043bd): "ExternalMap",
  ("old_space", 0x043e5): "JSMessageObjectMap",
  ("old_space", 0x0440d): "EmptyScript",
  ("old_space", 0x04455): "ManyClosuresCell",
  ("old_space", 0x04461): "ArrayConstructorProtector",
  ("old_space", 0x04475): "NoElementsProtector",
  ("old_space", 0x04489): "MegaDOMProtector",
  ("old_space", 0x0449d): "IsConcatSpreadableProtector",
  ("old_space", 0x044b1): "ArraySpeciesProtector",
  ("old_space", 0x044c5): "TypedArraySpeciesProtector",
  ("old_space", 0x044d9): "PromiseSpeciesProtector",
  ("old_space", 0x044ed): "RegExpSpeciesProtector",
  ("old_space", 0x04501): "StringLengthProtector",
  ("old_space", 0x04515): "ArrayIteratorProtector",
  ("old_space", 0x04529): "ArrayBufferDetachingProtector",
  ("old_space", 0x0453d): "PromiseHookProtector",
  ("old_space", 0x04551): "PromiseResolveProtector",
  ("old_space", 0x04565): "MapIteratorProtector",
  ("old_space", 0x04579): "PromiseThenProtector",
  ("old_space", 0x0458d): "SetIteratorProtector",
  ("old_space", 0x045a1): "StringIteratorProtector",
  ("old_space", 0x045b5): "NumberStringPrototypeNoReplaceProtector",
  ("old_space", 0x045c9): "StringSplitCache",
  ("old_space", 0x049d1): "RegExpMultipleCache",
  ("old_space", 0x04dd9): "BuiltinsConstantsTable",
  ("old_space", 0x053a9): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x053cd): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x053f1): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x05415): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x05439): "AsyncGeneratorYieldWithAwaitResolveSharedFun",
  ("old_space", 0x0545d): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x05481): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x054a5): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x054c9): "AsyncIteratorValueUnwrapSharedFun",
  ("old_space", 0x054ed): "PromiseAllResolveElementSharedFun",
  ("old_space", 0x05511): "PromiseAllSettledResolveElementSharedFun",
  ("old_space", 0x05535): "PromiseAllSettledRejectElementSharedFun",
  ("old_space", 0x05559): "PromiseAnyRejectElementSharedFun",
  ("old_space", 0x0557d): "PromiseCapabilityDefaultRejectSharedFun",
  ("old_space", 0x055a1): "PromiseCapabilityDefaultResolveSharedFun",
  ("old_space", 0x055c5): "PromiseCatchFinallySharedFun",
  ("old_space", 0x055e9): "PromiseGetCapabilitiesExecutorSharedFun",
  ("old_space", 0x0560d): "PromiseThenFinallySharedFun",
  ("old_space", 0x05631): "PromiseThrowerFinallySharedFun",
  ("old_space", 0x05655): "PromiseValueThunkFinallySharedFun",
  ("old_space", 0x05679): "ProxyRevokeSharedFun",
  ("old_space", 0x0569d): "ShadowRealmImportValueFulfilledSFI",
  ("old_space", 0x056c1): "SourceTextModuleExecuteAsyncModuleFulfilledSFI",
  ("old_space", 0x056e5): "SourceTextModuleExecuteAsyncModuleRejectedSFI",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x000c0000: "old_space",
  0x00000000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "WASM",
  "WASM_TO_JS",
  "WASM_TO_JS_FUNCTION",
  "JS_TO_WASM",
  "STACK_SWITCH",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_LIFTOFF_SETUP",
  "INTERPRETED",
  "BASELINE",
  "MAGLEV",
  "TURBOFAN",
  "STUB",
  "TURBOFAN_STUB_WITH_CONTEXT",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
