from_uuid_import_UUID  from_eth_typing_import_ChecksumAddress  from_empyrealSDK.exc_import_handle_response_error from_empyrealSDK.utils_import_RequestHelpers   class_SwapResource(RequestHelpers): async_def_ath( self, pair_address:_ChecksumAddress, chain_id:_int_=_1, ): response_=_await_self._get( "dex/ath", params={ "pairAddress":_pair_address, }, ) handle_response_error(response) return_response.json()  async_def_swap( self, path:_list[ChecksumAddress], amount_in:_int, wallet_id:_UUID, slippage_percent:_float_=_0.01, priority_fee:_int_=_0, is_private:_bool_=_False, chain_id:_int_=_1, use_eth:_bool_=_True, fees:_list[ChecksumAddress]_=_[], dex:_str_=_"uniswap", ): response_=_await_self._post( "dex/swap", json={ "path":_path, "amountIn":_amount_in, "walletId":_wallet_id, "slippage":_slippage_percent, "priorityFee":_priority_fee, "isPrivate":_is_private, "chainId":_chain_id, "useEth":_use_eth, "fees":_fees, "dex":_dex, }, ) handle_response_error(response) return_response.json()  async_def_simulate( self, path:_list[ChecksumAddress], amount_in:_int, sender:_ChecksumAddress, fees:_list[ChecksumAddress]_=_[], dex:_str_=_"uniswap", chain_id:_int_=_1, use_eth:_bool_=_True, ): response_=_await_self._put( "dex/simulate", json={ "dex":_dex, "path":_path, "fees":_fees, "amountIn":_str(amount_in), "sender":_sender, "chainId":_chain_id, "useEth":_use_eth, }, ) handle_response_error(response) return_response.json()