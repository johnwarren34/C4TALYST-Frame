import_gzip from_typing_import_Optional  from_eth_typing_import_HexAddress,_ChecksumAddress from_eth_utils.address_import_to_checksum_address  from_empyrealSDK.exc_import_handle_response_error from_empyrealSDK.utils_import_RequestHelpers   class_PriceResource(RequestHelpers): async_def_get_taxes( self, token_address:_ChecksumAddress, pair_token_address:_ChecksumAddress, dex:_str_=_"uniswap", chain_id:_int_=_1, ): response_=_await_self._put( "token/taxes", json={ "tokenAddress":_token_address, "pairToken":_pair_token_address, "chainId":_chain_id, "dex":_dex, }, ) handle_response_error(response) return_response.json()  async_def_get_routes( self, token_address:_ChecksumAddress, ): response_=_await_self._get( "dex/routes", params={ "startToken":_token_address, }, ) handle_response_error(response) return_response.json()  async_def_get_pair_info( self, pair_address:_HexAddress, force_checksum:_bool_=_True, chain_id:_int_=_1, ): """ Get_information_about_a_specific_pair_addresss """  if_force_checksum: pair_address_=_to_checksum_address(pair_address) response_=_await_self._get( "dex/pair", params={ "pairAddress":_pair_address, "chainId":_chain_id, }, ) return_response.json()  async_def_get_token_pairs( self, token_address:_HexAddress, chain_id:_int_=_1, force_checksum:_bool_=_True, ): if_force_checksum: token_address_=_to_checksum_address(token_address) response_=_await_self._get( "dex/pairs", params={ "tokenAddress":_token_address, "chainId":_chain_id, }, ) return_response.json()["pairs"]  async_def_get_liquidity( self, token_address:_HexAddress, chain_id:_int_=_1, force_checksum:_bool_=_True, block_number:_Optional[int]_=_None, ): if_force_checksum: token_address_=_to_checksum_address(token_address) response_=_await_self._put( "dex/liquidity", json={ "pairAddress":_token_address, "chainId":_chain_id, "blockNumber":_block_number, }, ) handle_response_error(response) return_response.json()  async_def_load_feed( self, pair_address:_ChecksumAddress, use_token0:_bool_=_True, start_time:_Optional[int]_=_None, end_time:_Optional[int]_=_None, ): response_=_await_self._get( "price/", params={ "pairAddress":_pair_address, "useToken0":_use_token0, }, ) handle_response_error(response) return_gzip.decompress(response.content).decode("utf-8")